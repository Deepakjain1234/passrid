from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from AuthPanel.models import PassitUser, WebsiteOwner, User
from ActivityPanel.models import Activity


def dashboard(request):
    params = {'range': range(10)}
    return render(request,'UserPanel/dashboard.html' , params)

def analytics(request):
    uid = request.user.id
    print(type(uid))
    passit_user = PassitUser.objects.get(user_id=7)
    print(uid)
    user_activity = Activity.objects.get(user_id=7)
    print(user_activity)
    params = {'name': passit_user.name , 'activity': user_activity , 'email': request.user.email , 'range': range(10)}
    return render(request,'UserPanel/analytics.html' , params)


@login_required
def userAccountDetails(request):
    id = request.user.id
    # passit_user = PassitUser.objects.get(user_id=id)
    print(id)

    return render(request,'UserPanel/account.html') 

def userLearn(request):
    return HttpResponse("<center><h2>This is the page for the User Learning</h2></center>")