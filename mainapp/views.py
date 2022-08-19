from django.shortcuts import render, redirect
from .models import Room, Message, Topic
from .forms import Roomform

# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q')!= None else ''
    
    room = Room.objects.filter(topic__name__icontains = q)
    topic = Topic.objects.all()
    context = {
        "rooms":room,
        "topics":topic
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

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = Roomform(instance=room)
    if request.method == 'POST':
        form = Roomform(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {
        "room":room,
        "form":form
    }
    return render(request, 'mainapp/newroom.html', context)

def delete(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'mainapp/del.html', {'obj':room})