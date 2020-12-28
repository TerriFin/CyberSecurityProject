from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Item

def rediredToIndex(request: HttpRequest):
    return redirect('/0/')

def index(request: HttpRequest, page):
    items_per_page = 6
    starting_index = page * items_per_page

    all_items = Item.objects.all()
    filtered_items = all_items[starting_index:][:items_per_page]

    return render(request, 'store/index.html', {
        'items': filtered_items,
        'page': page,
        'first_page': starting_index == 0,
        'last_page': starting_index + items_per_page >= len(all_items)}
    )

def login(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'store/login.html')

    if request.method == 'POST':
        try:
            user = authenticate(
                request,
                username=request.POST.get('name'),
                password=request.POST.get('password')
            )

            auth_login(request, user)
        except:
            return render(
                request,
                'store/login.html',
                {'error': 'Something went wrong while logging in'}
            )

    return redirect('/')

def logout(request: HttpRequest):
    if request.method == 'POST' and request.user.is_authenticated:
        auth_logout(request)

    return redirect('/')


def register(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'store/register.html')

    if request.method == 'POST':
        try:
            user = User.objects.create_user(
            request.POST.get('name'),
            request.POST.get('email'),
            request.POST.get('password'),)

            auth_login(request, user)
        except:
            return render(
                request,
                'store/register.html',
                {'error': 'Something went wrong while creating user'}
            )

    return redirect('/')
