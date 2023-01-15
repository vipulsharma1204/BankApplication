from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    
    # these two type of handlesignup one for GET method and another one is for POST methos
    path("", views.signup, name='signup'),
    path("login", views.login, name='login'),
    path("home", views.home, name='home'),
    path("signup", views.signup, name='signup'),
    path("form", views.form, name='form'),
    path("users", views.showUsers, name="showUsers"),
    path("searchDetails", views.searchDetails, name="searchDetails")
    
]
