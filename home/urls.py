from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    
    # these two type of handlesignup one for GET method and another one is for POST methos
    path("", views.handlesignup, name='signup'),
    path("login", views.login, name='login'),
    path("home", views.home, name='home'),
    path("signup", views.handlesignup, name='signup'),
    path("form", views.Formpage, name='login')
    ]
