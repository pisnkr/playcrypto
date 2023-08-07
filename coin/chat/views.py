# chat/views.py
from django.shortcuts import render, redirect
from .models import ChatRoom
from .forms import ChatRoomForm

def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

def chat_rooms(request):
    rooms = Room.objects.all()  # 모든 채팅방 정보 가져오기
    return render(request, 'chat/chat_rooms.html', {'rooms': rooms})

def create_chat_room(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat:chat_rooms')  # 채팅방 목록 페이지로 이동
    else:
        form = ChatRoomForm()
    return render(request, 'chat/create_chat_room.html', {'form': form})