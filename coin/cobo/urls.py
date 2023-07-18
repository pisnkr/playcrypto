# cobo/urls.py
from django.urls import path
from .views import base

app_name = 'cobo'

urlpatterns = [
    path('', views/base.board_list, name='board_list'),
    path('post/create/', views/base.post_create, name='post_create'),
    path('post_detail', views/base.post_detail, name='post_detail'),  # 새 게시물 작성 페이지 URL
]

