from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('' , views.homePage , name='homePage'),
  path('contact-us-submit/', views.contactUs , name='contactUs'),
  path('teams/' , views.teams , name='teams'),
  path('AboutUsDetail/' , views.aboutUsDetail , name='AboutUsDetail'),
  path('OurVision/' , views.ourVision , name='OurVision'),
]
 