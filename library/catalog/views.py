from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

from django.contrib import messages


@login_required
def catalog(request):
    context = {}
    return render(request, 'catalog/catalog.html', context)


@login_required
def home(request):
    context = {}
    return render(request, 'catalog/home.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = authenticate(request, username=username, password='Password1!')

        if user is not None:
            auth_login(request, user)
            return redirect('home')
    users = User.objects.filter(is_superuser=False)
    context = {
        'users': users,
    }
    return render(request, 'registration/login.html', context=context)

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        user = User.objects.create_user(username=username, password='Password1!')

        user = authenticate(request, username=user.username, password='Password1!')

        if user is not None:
            auth_login(request, user)
            return redirect('home')

    return redirect('login')
