from django import forms
from .models import Room

class RoomPost(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'roomtype', 'price', 'start_date', 'end_date', 'phonenumber', 'description', 'mainimg', 'img1', 'img2', 'img3']
        
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'(ex:깨끗한 집)'}),
            'roomtype' : forms.Select(attrs={'class':'form-control', 'placeholder':'(ex:원룸/투룸/아파트/고시텔/오피스텔)'}),
            'price' : forms.TextInput(attrs={'class':'form-control','placeholder':'가격을 입력하세요.'}),
            'start_date' : forms.TextInput(attrs={'class':'form-control','placeholder':'(ex: 2019-08-01)'}),
            'end_date' : forms.TextInput(attrs={'class':'form-control','placeholder':'(ex: 2019-08-31)'}),
            'phonenumber' : forms.TextInput(attrs={'class':'form-control','placeholder':'(ex: 01012345678  "-"제외)'}),
            'description' : forms.TextInput(attrs={'class':'form-control','style': 'height: 300px','placeholder':'방에 대한 설명을 입력하세요.'}),
        }

        labels = {
            'title': '제목',
            'roomtype': '방 종류',
            'price': '희망 가격',
            'start_date': '대여 시작일',
            'end_date': '대여 종료일',
            'phonenumber': '핸드폰 번호',
            'description': '설명',
            'mainimg': '대표사진',
            'img1': '사진1',
            'img2': '사진2',
            'img3': '사진3'
        }

class PostSearchForm(forms.Form) :
    search_word = forms.CharField(label = '검색어를 입력하세요')
