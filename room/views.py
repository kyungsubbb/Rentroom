from django.shortcuts import render, get_object_or_404,redirect
from .models import Room
from django.utils import timezone
from .form import RoomPost

def home(request):
    rooms = Room.objects
    return render(request, 'home.html', {'rooms':rooms})

def detail(request, room_id):
    details = get_object_or_404(Room, pk=room_id)
    return render(request, 'detail.html', {'room':details})

def register(request):
    return render(request,'register.html')

def create(request):
    room = Room()
    room.title = request.GET['title']
    room.roomtype = request.GET['roomtype']
    room.price = request.GET['price']    
    room.start_date = request.GET['start_date']
    room.end_date = request.GET['end_date']
    room.phonenumber = request.GET['phonenumber']
    room.description = request.GET['description']
    room.mainimg = request.GET['mainimg']
    room.img1 = request.GET['img1']
    room.img2 = request.GET['img2']
    room.img3 = request.GET['img3']
    room.save()
    return redirect('/room/' + str(room.id))

def roompost(request):
    if request.method == 'POST':
        form = RoomPost(request.POST)
        if form.is_valid():
            post.save()
            return redirect('home.html')

    else:
        form = RoomPost()
        return render(request,'register.html', {'form':form})    