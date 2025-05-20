from django.shortcuts import render,redirect, get_object_or_404
from Face_Detection.detection import FaceRecognition
from .forms import *
from django.contrib import messages
from FaceDetection.settings import BASE_DIR

faceRecognition = FaceRecognition()

def home(request):
    return render(request,'faceDetection/home.html')


from .models import UserProfile
import glob
import os

def register(request):
    if request.method == "POST":
        form = ResgistrationForm(request.POST, request.FILES)
        if form.is_valid():
            face_id = form.cleaned_data['face_id']

            # Capture face and train as you did...
            face_captured = faceRecognition.faceDetect(face_id)

            if face_captured:
                faceRecognition.trainFace()
                form.save()
                messages.success(request, "Successfully registered")
                return redirect('home')
            else:
                # Cleanup images and show error
                dataset_path = BASE_DIR + f'/Face_Detection/dataset/User.{face_id}.*.jpg'
                for file in glob.glob(dataset_path):
                    os.remove(file)
                messages.error(request, "Face not detected. Please try again.")
        else:
            messages.error(request, "Account registration failed")
    else:
        form = ResgistrationForm()
    return render(request, 'faceDetection/register.html', {'form': form})



def addFace(face_id):
    face_id = face_id
    faceRecognition.faceDetect(face_id)
    faceRecognition.trainFace()
    return redirect('/')

def login(request):
    face_id = faceRecognition.recognizeFace()
    if face_id is not None:
        return redirect('greeting', face_id)
    else:
        messages.error(request, "Face not recognized. Try again.")
        return redirect('home')



def greeting(request, face_id):
    face_id = int(face_id)
    user = get_object_or_404(UserProfile, face_id=face_id)
    return render(request, 'faceDetection/greeting.html', {'user': user})


def edit_profile(request, face_id):
    user = UserProfile.objects.get(face_id=face_id)

    if request.method == "POST":
        form = ResgistrationForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            # Check if new image is uploaded
            if 'image' in request.FILES:
                # Delete old image file if exists
                if user.image and os.path.isfile(user.image.path):
                    os.remove(user.image.path)

            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('greeting', face_id=face_id)
    else:
        form = ResgistrationForm(instance=user)

    return render(request, 'faceDetection/edit_profile.html', {'form': form, 'user': user})




def delete_profile(request, face_id):
    user = UserProfile.objects.get(face_id=face_id)
    user.delete()
    messages.success(request, "Profile deleted successfully.")
    return redirect('home')
