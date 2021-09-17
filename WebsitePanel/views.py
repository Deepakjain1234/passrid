from django.shortcuts import render
from django.http import HttpResponse


def websiteRegistration(request):
    return HttpResponse("<center><h2>This is the page for the website Registration</h2></center>")

def websiteLogin(request):
    return HttpResponse("<center><h2>This is the page for the website Login</h2></center>")


def websiteAccountDetails(request):
    return HttpResponse("<center><h2>This is the page for the website Account Detail</h2></center>")

def websiteLearn(request):
    return HttpResponse("<center><h2>This is the page for the website Learning</h2></center>")

