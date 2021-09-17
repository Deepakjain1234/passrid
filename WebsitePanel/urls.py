from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.websiteRegistration , name='websiteRegistration'),
    path('WebsiteLogin/' , views.websiteLogin , name='websiteLogin'),
    path('WebisteAccountDetails/' , views.websiteAccountDetails , name='websiteAccountDetails'),
    path('WebsiteLearn/' , views.websiteLearn , name='websiteLearn'),
]