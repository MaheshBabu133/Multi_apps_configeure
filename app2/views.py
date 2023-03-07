from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def First_app2(request):
    return HttpResponse('<h1>my first app_2 function</h1>')
def Second_app2(request):
    return HttpResponse('<h1>my second app_2 function</h1>')