# chat/urls.py
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path('chat_rooms/', views.chat_rooms, name='chat_rooms'),
    path('create_chat_room/', views.create_chat_room, name='create_chat_room'),

]
