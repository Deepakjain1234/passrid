from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('UserAccountDetails/', views.userAccountDetails, name='userAccountDetails'),
  path('UserLearn/', views.userLearn, name='userLearn'),
  path('dashboard/',views.dashboard, name='dashboard'),
  path('analytics/',views.analytics, name='analytics')
]
 