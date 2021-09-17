from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail, BadHeaderError


def homePage(request):
    return render(request, 'PassitPanel/homePage.html')

def teams(request):
    return render(request, 'PassitPanel/teams.html')     

def ourVision(request):
    return render(request, 'PassitPanel/ourVision.html')  

def aboutUsDetail(request):
    return render(request, 'PassitPanel/aboutUsDetail.html')
 

def contactUs(request):
    if request.method == 'POST':
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        message = request.POST.get('message', "")

        # now from here we will store the contact information in the databases
        # for future reference and will also store time stamp and server details.

        print(name, email, message)

        # Now here we will send mail to the person who sent the message to us.
        # Also here we need to create a class for email backend to provide password and host email and port no for sending the mail........
        if subject and message and from_email:
            try:
                send_mail(
                    'Passit team will connect with you soon',
                    'Thank you {name} for messaging us and out team will shortly coonect with you and will solve your query.',
                    'sourabhmishra1262@gmail.com',
                    [email],
                    fail_silently=False,
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse("Thank you for contacting")

        else:
            return HttpResponse('Make sure all fields are entered and valid.')
# Create your views here.
