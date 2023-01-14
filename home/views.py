from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
from home.models import UserDetail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext
import re
from datetime import*

def login(request):
    return render(request, 'VIEWS/login.html', {"":""} )

def home(request):
    return render(request, 'VIEWS/home.html',{"":""})

def form(request):
    
    # this is for GET method
    if request.method=="GET":
        return render(request, 'VIEWS/form.html')
    
    # this is for POST method
    if request.method=='POST':
        
        namePrefix=request.POST.get('courtsey',"")        
        fname=request.POST.get('firstName',"")
        mname=request.POST.get('middlename',"")
        lname=request.POST.get('lastName',"")
        email=request.POST.get('email',"")
        contact=str(request.POST.get('contact',""))
        alternatenumber=str(request.POST.get('alternatenumber',""))        
        address=request.POST.get('address',"")
        mothername=request.POST.get('motherName',"")
        fatherName=request.POST.get('fatherName',"")
        pincode=request.POST.get('pinCode',191)
        dob=request.POST.get('dob',"")
        PAN=request.POST.get('panNumber',"")
        aadhaar=request.POST.get('aadhaarNumber',"")
        occupation=request.POST.get('occupation',"")
        relation=request.POST.get('relation',"")
        accounttype=request.POST.get('MemeberType',"")    
        myuser = UserDetail()
        myuser.namePrefix=namePrefix    
        myuser.firstName=fname            
        myuser.middleName=mname           
        myuser.lastName=lname
        myuser.email=email 
        myuser.phoneNumber=contact
        myuser.alternatePhoneNumber=alternatenumber           
        myuser.address=address            
        myuser.motherName=mothername            
        myuser.fatherName=fatherName         
        myuser.zipCode=pincode            
        myuser.dateOfBirth=dob            
        myuser.panNumber=PAN            
        myuser.aadhaarNumber=aadhaar        
        myuser.occupation=occupation            
        myuser.relation=relation         
        myuser.accountType=accounttype
        myuser.save()
        return render(request, 'VIEWS/home.html', {"username":myuser.username})

def signup(request):
    if request.method=="GET":
        return render(request, 'VIEWS/Signup.html', {"error":""})
    
    if request.method=='POST':
        fname=request.POST.get('fname',"")
        lname=request.POST.get('lname',"")        
        username=request.POST.get('username',"") 
        address=request.POST.get('address',"")
        contact=request.POST.get('contact',"")
        email=request.POST.get('emailId',"")
        password=request.POST.get('loginpassword',"")
        password1=request.POST.get('loginpassword1',"")
        
          
        if not username.isalnum():
            return render(request, "VIEWS/Signup.html", {"error":"your username must contains only chars and digits"})
        
        if len(address)>250:
            return render(request, "VIEWS/Signup.html", {"error":"Max 250 chars allowed in address"})
            
        if password!=password1:
            return render(request, "VIEWS/Signup.html", {"error":"Password mismatch"})
        
        elif len(password)<=8 or len(password)>=64:
            return render(request, "VIEWS/Signup.html", {"error":"Password length should be between 8 to 64 chars"})
        
        myuser=UserDetail()
        myuser.UserName=username
        myuser.firstname=fname
        myuser.lastname=lname
        myuser.Email=email
        myuser.save()
        return render(request, "VIEWS/form.html", {"error":""})
    
    return redirect(login)

def showUsers(request):
    if request.method=="GET":
        return render(request, "VIEWS/users.html", {"users": UserDetail.objects.all()})
