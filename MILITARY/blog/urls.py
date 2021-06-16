from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('about', views.About.as_view(), name='about'),
    path('about', views.about, name='about'),
    path('realhome', views.realhome, name='realhome'),
    path('services', views.service, name='services'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup')
]