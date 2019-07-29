from django import forms
from .models import Room

class RoomPost(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'roomtype', 'price', 'start_date', 'end_date', 'phonenumber', 'description', 'mainimg', 'img1', 'img2', 'img3']