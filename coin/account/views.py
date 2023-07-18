from django.shortcuts import render

def login(request):
    return render(request, 'account/login.html')

def password(request):
    return render(request, 'account/password.html')

def register(request):
    return render(request, 'account/register.html')

