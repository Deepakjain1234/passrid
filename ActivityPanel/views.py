from django.shortcuts import render
from .models import Activity
from .serializer import ActivitySerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def activityDetail(request):
    # sending the data for just one user for now...
    complex_data = Activity.objects.get(user_id='7')
    # complex data
    serializer = ActivitySerializer(complex_data)
    # complex data --> python data
    json_data = JSONRenderer().render(serializer.data)
    # python data --> json data

    return HttpResponse(json_data, content_type='application/json')
