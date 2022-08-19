from django.shortcuts import render
from .models import Room, Message


# Create your views here.

def home(request):
    room = Room.objects.all()
    context = {
        "rooms":room
    }
    
    return render(request, 'mainapp/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    message = Message.objects.filter(room__id = pk).all()
    context = {
        "room" : room,
        "message":message
    }
    return render(request, 'mainapp/room.html', context)