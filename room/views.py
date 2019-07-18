from django.shortcuts import render, get_object_or_404
from .models import Room

def home(request):
    rooms = Room.objects
    return render(request, 'home.html', {'rooms':rooms})

def register(request):
    return render(request, 'register.html')