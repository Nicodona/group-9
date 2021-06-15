from django.shortcuts import render
from django.views.generic import ListView

# class home(ListView):
#     template_name = 'index.html'

def home(request):
    return render(request, 'index.html')

def realhome(request):
    return render(request, 'home.html')

def service(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')