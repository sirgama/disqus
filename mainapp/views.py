from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Room, Message, Topic
from .forms import Roomform

# Create your views here.
def LogView(request):
    page = 'log'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request, 'User Does Not Exist.')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Username or password Does Not Exist.')
        
    context = {
        'page':page
    }
    return render(request, 'mainapp/login.html', context)
def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    context = {
        "form":form
    }
    return render(request, 'mainapp/login.html', context)
    

def home(request):
    q = request.GET.get('q') if request.GET.get('q')!= None else ''
    
    
    room = Room.objects.filter(Q(topic__name__icontains = q) | Q(name__icontains=q) | Q(description__icontains=q) | Q(host__username__icontains=q))
    topic = Topic.objects.all()
    all_messages = Message.objects.filter(Q(room__topic__name__icontains=q)).order_by('-created')
    context = {
        "rooms":room,
        "topics":topic,
        "texts":all_messages
    }
    
    return render(request, 'mainapp/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    roomchats = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)
    context = {
        "room" : room,
        "roomchats":roomchats,
        "members":participants
    }
    return render(request, 'mainapp/room.html', context)


def userProfie(request, pk):
    user = User.objects.get(username=pk)
    rooms= user.room_set.all()
    texts = user.message_set.all()
    topics = Topic.objects.all()
    context = {
        "user":user,
        "rooms":rooms,
        "texts":texts,
        "topics":topics
    }
    
    return render(request, 'mainapp/userprofile.html', context)


@login_required(login_url='log')
def newroom(request):
    form = Roomform()
    if request.method == 'POST':
        form = Roomform(request.POST)
        if form.is_valid:
        
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect('home')
        print(request.POST)
    context = {
        "form":form
    }
    
    return render (request, 'mainapp/newroom.html', context)

@login_required(login_url='log')
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

@login_required(login_url='log')
def delete(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'mainapp/del.html', {'obj':room})

@login_required(login_url='log')
def deleteMessage(request, pk):
    text = Message.objects.get(id=pk)
    if request.user!=text.user:
        return HTTPResponse("You are not allowed to access this function")
    if request.method == 'POST':
        text.delete()
        return redirect('home')
    return render(request, 'mainapp/del.html', {'obj':text})