from django.shortcuts import render

# Create your views here.

# chat/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Django Chat App!")
