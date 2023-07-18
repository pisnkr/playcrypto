# cobo/urls.py
from django.urls import path
from .views import base

app_name = 'cobo'

urlpatterns = [
    path('', base.board_list, name='board_list'),
    path('post/create/', base.post_create, name='post_create'),
    path('post_detail', base.post_detail, name='post_detail'),  # 새 게시물 작성 페이지 URL
]

