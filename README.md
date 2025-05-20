# Face Recognition Login System with Django and OpenCV

This project is a facial recognition-based login and registration system built using Django and OpenCV. It allows users to register with their facial data and log in using real-time face detection via webcam.

## 🔧 Features

- Face Registration via webcam
- Face Login using OpenCV
- User profile management (CRUD)
- Image-based user authentication
- Django-based web interface

## 📂 Project Structure

registration-login/
├── Face_Detection/ # Django app with views, models, forms
├── FaceDetection/ # Main project folder with settings.py
├── templates/ # HTML templates
├── media/ # Media files
└── manage.py


# Requirements
- Basic Django
- Basic Python and knowledge about OOP
- A good IDE like VSCode

# Instalisation

- Linux:
``` pip3 install django ```

``` pip3 in opencv-python==3.4.2.17 ```

- Windows:
``` pip install django ```

``` pip3 in opencv-python==3.4.2.17 ```


# 🚀 How to Run the Project
Clone the repo (if not already):

``` git clone https://github.com/yourusername/your-repo-name.git ```
``` cd your-repo-name ```
``` Create a virtual environment (optional but recommended): ```

# Project creation command:
``` django-admin startproject FaceDetection```

# Important command for this project-
``` python3 manage.py startapp Face_Detection ``` - **For Creating App**  
``` python3 manage.py makemigrations``` - **Migrations Model**  
``` python3 manage.py migrate```- **For migrating to Database** 
``` python3 manage.py runserver```- **For running server** 

# Open your browser and go to:
http://127.0.0.1:8000/

# Descriptions
This is an ML-based face recognition system. Using that we can register and recognize the face of a person.

