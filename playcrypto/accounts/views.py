from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def signup(request):
    # 회원가입 로직 구현
    return render(request, 'signup.html')

def login(request):
    # 로그인 로직 구현
    return render(request, 'login.html')

def logout(request):
    # 로그아웃 로직 구현
    return render(request, 'logout.html')


