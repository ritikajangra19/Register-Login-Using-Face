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
- Basic Python and knowledge of OOP
- A good IDE like VSCode
- Knowledge on Opencv and face_recognition

# Installation Requirements

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


# Important command for this project-

``` python manage.py createsuperuser``` - **Creates superuser**

``` python3 manage.py makemigrations``` - **Migrations Model**  

``` python3 manage.py migrate```- **For migrating to Database** 

``` python3 manage.py runserver```- **For running server** 


# Open your browser and go to:

http://127.0.0.1:8000/

# UI:

**Home Page**

<img width="959" alt="home page" src="https://github.com/user-attachments/assets/49fbe7e3-1a45-4d3c-b565-59f4c19f3a3e" />

**Registration page** 

<img width="943" alt="registration1" src="https://github.com/user-attachments/assets/71cb7ad2-e33a-456d-ba3d-015363938ee4" />


**Registration Page**

<img width="938" alt="registration2" src="https://github.com/user-attachments/assets/8e9adcf4-1dec-4b45-9887-eeb5a4765616" />

**Greetings Page**

<img width="953" alt="image" src="https://github.com/user-attachments/assets/2e433b97-9c3c-48d2-b2db-0a7d9decea2d" />



# Descriptions

This is an ML-based face recognition system. Using that we can register and recognize the face of a person.

