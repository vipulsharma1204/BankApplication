from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    # these two type of handlesignup one for GET method and another one is for POST methos
    path("", views.signup, name='signup'),
    
    path('login', views.login, name='login'),
    path('home', views.identify, name='home'),
    path('users', views.showUsers, name="users"),
    path('adduser', views.adduser, name='adduser'),
    path('transaction', views.transaction, name='transaction'),
    path('help', views.help, name='help'),
    path('update', views.update, name='update'),
    path('credit', views.credit, name='credit'),
    path('debit', views.debit, name='debit'),
    path("updateUserDetails", views.updateUserDetails, name="updateUserDetails"),
    path("searchDetails", views.searchDetails, name='searchDetails'),
    path("form", views.form, name='form'),
    # path('aadmin',views.aadmin name='aadmin')
   
    
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
