from django.shortcuts import render, redirect
from .models import Room, Message
from .forms import Roomform

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

def newroom(request):
    form = Roomform()
    if request.method == 'POST':
        form = Roomform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
        print(request.POST)
    context = {
        "form":form
    }
    
    return render (request, 'mainapp/newroom.html', context)