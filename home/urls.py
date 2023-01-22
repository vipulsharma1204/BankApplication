from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    
    # these two type of handlesignup one for GET method and another one is for POST methos
    path("", views.signup, name='signup'),
    
    path('login', views.login, name='login'),
    path('home', views.identify, name='home'),
    path('adduser', views.adduser, name='adduser'),
    path('transaction', views.transaction, name='transaction'),
    path('help', views.help, name='help'),
    path('update', views.update, name='update'),
    path('credit', views.credit, name='credit'),
    path('debit', views.debit, name='debit'),
    
    path("form", views.form, name='form'),
    # path('aadmin',views.aadmin name='aadmin')
   
    
]
