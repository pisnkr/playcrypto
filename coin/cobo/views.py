from django.shortcuts import render

def board_list(request):
    return render(request, 'cobo/board_list.html')

def post_create(request):
    return render(request, 'cobo/post_create.html')

def post_detail(request):
    return render(request, 'cobo/post_detail.html')


