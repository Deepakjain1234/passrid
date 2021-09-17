from django.contrib import admin 
from django.urls import path, include
from django.conf import settings
from . import views
 
urlpatterns = [
    path('UserLoginRegister' , views.UserLoginRegister , name='userLoginRegister'),
    path('WebsiteLoginRegister' , views.WebsiteLoginRegister , name='websiteLoginRegister'),
    path('UserLogout' , views.userLogout , name='userLogout'),
]