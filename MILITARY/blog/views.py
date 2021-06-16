from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Feed
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse_lazy

# class home(ListView):
#     template_name = 'index.html'

def home(request):
    return render(request, 'index.html')

def realhome(request):
    return render(request, 'home.html')

def service(request):
    return render(request, 'services.html')

def about(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        feed = Feed(name=name, email=email, Message=message)
        feed.save()
        return redirect('/')
    else:
        return render(request, 'about.html')



def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        passwd1 = request.POST['passwd1']
        passwd2 = request.POST['passwd2']
        email = request.POST['email']

        if passwd1 == passwd2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username exit')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=passwd1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password did not match')
            return redirect('signup')
    else:
        return render(request, 'register/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'wrong credentials please try again')
            return redirect('login')
    else:
        return render(request, 'register/login.html')
