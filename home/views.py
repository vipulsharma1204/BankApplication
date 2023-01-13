from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.password_validation import validate_password

# from home.models import Contact
from django.contrib import messages
from home.models import UserDetail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext
import re
from datetime import*


# Create your views here.


# path("login", views.login, name='login'),
def login(request):
    return render(request, 'VIEWS/login.html', {"":""} )


# path("home", views.home, name='home'),
def home(request):
    return render(request, 'VIEWS/home.html',{"":""})


def Formpage(request):
    
    # this is for GET method
    if request.method=="GET":
        return render(request, 'VIEWS/form.html')
    
    # this is for POST method
    if request.method=='POST':
        namePrefix=request.POST.get('courtsey',"")
        
        fname=request.POST.get('firstName',"")
        if not bool(re.match("^[a-zA-Z]{2,56}$", fname)):
            return render(request, "VIEWS/form.html", {"error":"Please enter your corret name."})                     
            
            
        mname=request.POST.get('middlename',"")
        if not bool(re.match("^[a-zA-Z]{0,56}$", mname)):
            return render(request, "VIEWS/form.html", {"error":"Please enter your corret middle name."})
        
        lname=request.POST.get('lastName',"")
        if not bool(re.match("^[a-zA-Z]{4,256}$", lname)):
            return render(request, "VIEWS/form.html", {"error":"Please enter your corret Surname."})
        
        contact=str(request.POST.get('contact',""))
        if len(contact)!=10:
            return render(request, "VIEWS/form.html", {"error":"Please enter your Correct Contact Details."})
        
        alternatenumber=str(request.POST.get('alternatenumber',""))
        if len(alternatenumber)!=10:
            return render(request, "VIEWS/form.html", {"error":"Please enter your Correct alternatenumber Details."})
            
        
        address=request.POST.get('address',"")
        
        mothername=request.POST.get('motherName',"")
        if not bool(re.match("^[a-zA-Z ]{6,128}$", mothername)):
            return render(request, "VIEWS/form.html", {"error":"Please enter your correct Mother Name."})
        
        fatherName=request.POST.get('fatherName',"")
        if not bool(re.match("^[a-zA-Z ]{6,128}$", fatherName)):
            return render(request, "VIEWS/form.html", {"error":"Please enter your correct Father Name."})
        
        pincode=request.POST.get('pinCode',191)
        if not bool(re.match("^[0-9 ]{4,10}$", pincode)):
            return render(request, "VIEWS/form.html", {"error":"Please enter your correct Zip Code."})
            
        dob=request.POST.get('dob',"")
        
                
        PAN=request.POST.get('panNumber',"")
        if len(PAN)!=10:
            return render(request, "VIEWS/form.html", {"error":"Enter correct PAN NUmber. "})
            
        aadhaar=request.POST.get('aadhaarNumber',"")
        if len(aadhaar)!=12:
            return render(request, "VIEWS/form.html", {"error":"Enter correct Aadhaar Number. "})
            
        occ=request.POST.get('occ.',"")
        if not bool(re.match("^[a-zA-Z]{4,128}$", occ)):
            return render(request, "VIEWS/form.html", {"error":"Please enter your correct Occupation."})
            
        relation=request.POST.get('relation',"")
        if not bool(re.match("^[a-zA-Z]{3,128}$", relation)):
            return render(request, "VIEWS/form.html", {"error":"Please enter your relationship with Applicant."})
            
        print(namePrefix)
        accounttype=request.POST.get('MemeberType',"")
        
        
        
        if not bool(re.match("^[a-zA-Z]{4,24}$", fname)):
            return render(request, "VIEWS/form.html", {"error":"Please enter your correct Details ."})
        else:         
            myuser = UserDetail()
            myuser.nameprefix=namePrefix    
            myuser.firstName=fname            
            myuser.middlename=mname           
            myuser.lastName=lname 
            myuser.phoneNo=contact
            myuser.alternatePhoneNumber=alternatenumber           
            myuser.address=address            
            myuser.motherName=mothername            
            myuser.Fathername=fatherName         
            myuser.zipcode=pincode            
            myuser.dateOfBirth=dob            
            myuser.panNumber=PAN            
            myuser.aadhaarNumber=aadhaar        
            myuser.occupation=occ            
            myuser.RELATION=relation         
            myuser.accountType=accounttype
            myuser.save()
    return render(request, 'VIEWS/home.html')
    # return redirect(home)
    # return render(request, "VIEWS/home.html", {"":""})
    # return render(request, "VIEWS/home.html", {"username":lname+", "+fname})


        
        
        
        
        
        
    
    
def handlesignup(request):
    if request.method=="GET":
        return render(request, 'VIEWS/Signup.html', {"error":""})
    if request.method=='POST':
        fname=request.POST.get('fname',"")
        lname=request.POST.get('lname',"")
        
        username=request.POST.get('username',"")   
        if len(username)<=10 or len(username)>128:
            return render(request, "VIEWS/Signup.html", {"error":"Please choose a username of min. 10 and max. 128 character"})
        elif not username.isalnum():
            return render(request, "VIEWS/Signup.html", {"error":"your username must contains number."})
            
                
        address=request.POST.get('address',"")
        
        if len(address)<=20 or len(address)>250:
            return render(request, "VIEWS/Signup.html", {"error":"please enter a correct address"})
        
        
        contact=request.POST.get('contact',"")
        # print(contact, type(contact))
        
        if len(contact)!=10:
            print(contact)
            return render(request, "VIEWS/Signup.html", {"error":"contact number must be of 10 digit"})
            
            
        email=request.POST.get('emailId',"")
        password=request.POST.get('loginpassword',"")
        password1=request.POST.get('loginpassword1',"")
        
        if password!=password1:
            print(len(password))
            # print(password, password1)
            return render(request, "VIEWS/Signup.html", {"error":"Password mismatch"})
        elif len(password)<=8:
            return render(request, "VIEWS/Signup.html", {"error":"Please suggest a strong password"})
        elif len(password)>=64:
            return render(request, "VIEWS/Signup.html", {"error":"Password length mist be less than 64 character"})
        elif not password.isalnum():
            return render(request, "VIEWS/Signup.html", {"error":"Please set a password which contains alphanumeric"})
            
            
            
            
            
        else:
            # print("POST Method : ", request.POST)
            # myuser= User.objects.create_user(username,email,password)
            myuser=UserDetail()
            myuser.UserName=username
            myuser.firstname=fname
            myuser.lastname=lname
            myuser.Email=email
            myuser.save()
            return render(request, "VIEWS/form.html", {"error":""})
    return redirect(login)
        
        
        
        
    
    
