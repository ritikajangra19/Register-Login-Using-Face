
from django.urls import path
from .views import *
urlpatterns = [
    path('', home,name = "home"),
    path('register/', register,name = 'register'),
    path('login/', login,name = 'login'),
    path('greeting/<face_id>/',greeting,name='greeting'),
    path('edit/<int:face_id>/', edit_profile, name='edit_profile'),
    path('delete/<int:face_id>/', delete_profile, name='delete_profile'),
]
