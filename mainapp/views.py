from django.shortcuts import render

# Create your views here.
rooms = [
    {"id":1, "name": "Nthe first"},
    {"id":2, "name": "Second"},
    {"id":3, "name": "Third one"}
]

def home(request):
    context = {
        "rooms":rooms
    }
    
    return render(request, 'mainapp/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {
        "room" : room
    }
    return render(request, 'mainapp/room.html', context)