from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm, WebsiteRegForm, AuthenticationForm
from django.views.decorators.csrf import csrf_protect

from AuthPanel.models import User


@csrf_protect
def WebsiteLoginRegister(request):

    # Checking if user is already authenticated
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("userAccountDetails"))

    # Clearing existing sessions
    request.session.flush()

    # Forms for registration and login
    regform = WebsiteRegForm()
    loginform = AuthenticationForm()

    # Handling multiple requests from same page
    if request.method == "POST":

        # Checking for register request
        if request.POST.get('submit') == 'Register':

            regform = WebsiteRegForm(request.POST)
            # Checking for form validity using is_valid() func (pre-defined)
            if regform.is_valid():
                regform.save()

                domain = regform.cleaned_data.get('domain')
                messages.success(
                    request, f'Your domain {domain} is now registered with us! Please login to continue.')

                return HttpResponseRedirect(reverse("websiteLoginRegister"))

            # Handling form error case
            else:
                messages.warning(request, 'Registration unsuccessful!')
                return HttpResponseRedirect(reverse("websiteLoginRegister"))

        # Checking for login request
        elif request.POST.get('submit') == 'Login':

            form = AuthenticationForm(data=request.POST)
            if form.is_valid():

                user = User.objects.get(email=request.POST["username"])

                if not user.is_websiteowner:
                    loginform = AuthenticationForm(request.POST)
                    messages.warning(request, 'Invalid Credentials')
                    return render(request, 'AuthPanel/website.html', {
                        'regform': regform,
                        'loginform': loginform,
                    })

                if form.cleaned_data.get('remember_me'):
                    request.session.set_expiry(604800)

                # Okay, security checks complete. Log the user in.
                login(request, form.get_user())
                return HttpResponseRedirect(reverse("userAccountDetails"))

            # Handling errors in user model
            else:
                loginform = AuthenticationForm(request.POST)
                messages.warning(request, 'Invalid Credentials')
                return render(request, 'AuthPanel/website.html', {
                    'regform': regform,
                    'loginform': loginform,
                })
    # GET request
    else:
        return render(request, "AuthPanel/website.html", {
            'regform': regform,
            'loginform': loginform,
        })


@csrf_protect
def UserLoginRegister(request):

    # Checking if user is already authenticated
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("dashboard"))

    # Clearing existing sessions
    request.session.flush()

    # Forms for registration and login
    regform = CreateUserForm()
    loginform = AuthenticationForm()

    # Handling multiple requests from same page
    if request.method == "POST":

        # Checking for register request
        if request.POST.get('submit') == 'Register':
            regform = CreateUserForm(request.POST)

            # Checking for form validity using is_valid() func (pre-defined)
            if regform.is_valid():
                regform.save()

                username = regform.cleaned_data.get('first_name')
                messages.success(
                    request, f'Account created successfully for {username}! Please login to continue.')
                return HttpResponseRedirect(reverse("userLoginRegister"))

            # Handling form error case
            else:
                messages.warning(request, 'Registration unsuccessful!')
                return HttpResponseRedirect(reverse("userLoginRegister"))

        # Checking for login request
        elif request.POST.get('submit') == 'Login':

            form = AuthenticationForm(data=request.POST)
            if form.is_valid():

                user = User.objects.get(email=request.POST["username"])

                if not user.is_passituser:
                    messages.warning(request, 'Invalid Credentials')
                    return render(request, 'AuthPanel/user.html', {
                        'regform': regform,
                        'loginform': loginform,
                    })

                if form.cleaned_data.get('remember_me'):
                    request.session.set_expiry(604800)

                # Okay, security checks complete. Log the user in.
                login(request, form.get_user())
                return HttpResponseRedirect(reverse("dashboard"))

            # Handling errors in user model
            else:
                messages.warning(request, 'Invalid Credentials')
                return render(request, 'AuthPanel/user.html', {
                    'regform': regform,
                    'loginform': loginform,
                })
    else:
        # GET request
        return render(request, "AuthPanel/user.html", {
            'regform': regform,
            'loginform': loginform,
        })


@login_required
def userActivity(request):
    return HttpResponse("<center><h2>This is the page for the User Activity</h2></center>")


def userLearn(request):
    return HttpResponse("<center><h2>This is the page for the User Learning</h2></center>")


@login_required
def userLogout(request):
    logout(request)
    request.session.flush()
    messages.success(request, 'Logged Out!')
    return HttpResponseRedirect(reverse("userLoginRegister"))
