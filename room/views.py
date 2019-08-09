from django.shortcuts import render, get_object_or_404,redirect
from .models import Room
from django.utils import timezone
from .forms import RoomPost
from django.views.generic.edit import FormView
from room.forms import PostSearchForm
from django.db.models import Q

def first(request):
    return render(request, 'first.html')

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
        form = RoomPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.sample5_address = request.POST.get('sample5_address')
            post.save()
            return redirect('home')
    else:
        form = RoomPost()
    return render(request,'register.html', {'form':form})



class SearchFormView(FormView):
    # form_class를 forms.py에서 정의했던 PostSearchForm으로 정의
    form_class = PostSearchForm
    template_name = 'search.html'#search.html

    # 제출된 값이 유효성검사를 통과하면 form_valid 메소드 실행
    # 여기선 제출된 search_word가 PostSearchForm에서 정의한대로 Char인지 검사
    def form_valid(self, form):
        # 제출된 값은 POST로 전달됨
        # 사용자가 입력한 검색 단어를 변수에 저장
        search_word = self.request.POST['search_word']
        # Post의 객체중 제목이나 설명이나 내용에 해당 단어가 대소문자관계없이(icontains) 속해있는 객체를 필터링
        # Q객체는 |(or)과 &(and) 두개의 operator와 사용가능
        post_list = Room.objects.filter(Q(description__icontains=search_word) | Q(title__icontains=search_word)    )

        context = {}
        # context에 form객체, 즉 PostSearchForm객체 저장
        context['form'] = form
        context['search_term'] = search_word
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)
