from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def First_app1(request):
    return HttpResponse('<h1>my first app_1 function</h1>')
def Second_app1(request):
    return HttpResponse('<h1>my second app_1 function</h1>')