from urllib import request, response
from django.shortcuts import render

# Create your views here.

def home(request):
    
    
    return render(request, 'mainapp/home.html')

def room(request):
    
    
    return render(request, 'mainapp/room.html')