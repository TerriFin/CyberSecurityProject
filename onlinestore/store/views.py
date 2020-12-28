from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Item
from .forms import ItemForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

def rediredToIndex(request: HttpRequest):
    return redirect('/0/')

def index(request: HttpRequest, page):

    items_per_page = 6
    starting_index = page * items_per_page

    if request.method == 'POST':
        # Use .raw so that sql injections work :-D
        items = Item.objects.raw("SELECT * FROM store_item WHERE description LIKE '%%{0}%%'".format(request.POST.get('query')))
        print('FOUND WITH QUERY ' + str(items))
        for r in items:
            print(r)
    else:
        items = Item.objects.all()

    filtered_items = items[starting_index:][:items_per_page]

    return render(request, 'store/index.html', {
        'items': filtered_items,
        'page': page,
        'first_page': starting_index == 0,
        'last_page': starting_index + items_per_page >= len(items)}
    )

def login(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'store/login.html')
    elif request.method == 'POST':
        try:
            user = authenticate(
                request,
                username=request.POST.get('name'),
                password=request.POST.get('password')
            )

            auth_login(request, user)
        except Exception as e:
            print(e)
            return render(
                request,
                'store/login.html',
                {'error': 'Something went wrong while logging in'}
            )

    return redirect('/')

def register(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'store/register.html')
    elif request.method == 'POST':
        try:
            user = User.objects.create_user(
                request.POST.get('name'),
                request.POST.get('email'),
                request.POST.get('password'),
            )

            return redirect('/login/')
        except:
            return render(
                request,
                'store/register.html',
                {'error': 'Something went wrong while creating user'}
            )

def logout(request: HttpRequest):
    if request.method == 'POST' and request.user.is_authenticated:
        auth_logout(request)

    return redirect('/')

def manager(request: HttpRequest):

    perm = Permission.objects.get(codename="manager")

    if request.method == 'GET':
        non_managers = User.objects.filter(~Q(user_permissions=perm))
        managers = User.objects.filter(Q(user_permissions=perm))

        return render(
            request,
            'store/manager.html',
            {
                'non_managers': non_managers,
                'managers': managers,
                # This was a test, it worked but the old system worked and i already styled it so it is good enough :-D
                # Feel free to remove the comment and see what it does!
                #'form': ItemForm()
            }
        )
    elif request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST.get('user'))
            if request.POST.get('function') == 'add':
                user.user_permissions.add(perm)
            elif request.POST.get('function') == 'delete':
                user.user_permissions.remove(perm)
        except:
            return render(
                request,
                'store/manager.html',
                {'error': 'Please select user to promote or demote'}
            )
    return redirect('/manager/')

def uploadItem(request: HttpRequest):
    if request.method == 'POST' and request.FILES.get('image'):
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return redirect('/manager/')
