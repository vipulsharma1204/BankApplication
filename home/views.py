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
        contact=str(request.POST.get('contact',""))
        alternatenumber=str(request.POST.get('alternatenumber',""))        
        address=request.POST.get('address',"")
        mothername=request.POST.get('motherName',"")
        fatherName=request.POST.get('fatherName',"")
        pincode=request.POST.get('pinCode',191)
        dob=request.POST.get('dob',"")
        PAN=request.POST.get('panNumber',"")
        aadhaar=request.POST.get('aadhaarNumber',"")
        occupation=request.POST.get('occupation.',"")
        relation=request.POST.get('relation',"")
        accounttype=request.POST.get('MemeberType',"")
        
        if not bool(re.match("^[a-zA-Z]{2,56}$", fname)):
            return render(request, "VIEWS/form.html", {"error":"First name should be between 2 to 56 chars"})  
            
        if mname!=None and not bool(re.match("^[a-zA-Z]{0,56}$", mname)):
            return render(request, "VIEWS/form.html", {"error":"Middle name should be between 2 to 56 chars"})
        
        if not bool(re.match("^[a-zA-Z]{2,56}$", lname)):
            return render(request, "VIEWS/form.html", {"error":"Last name should be between 2 to 56 chars."})        
        
        if not bool(re.match("^[a-zA-Z, ]{2,128}$", mothername)):
            return render(request, "VIEWS/form.html", {"error":"Mothers name should be between 2 to 128 chars."})
        
        if not bool(re.match("^[a-zA-Z, ]{2,128}$", fatherName)):
            return render(request, "VIEWS/form.html", {"error":"Fathers name should be between 2 to 128 chars"})
        
        if not bool(re.match("^[\d]{4,10}$", pincode)):
            return render(request, "VIEWS/form.html", {"error":"Pin code should be of 4 to 10 digits"})
            
        if len(PAN)!=10:
            return render(request, "VIEWS/form.html", {"error":"PAN Number should be of exactly 10  digits"})
            
        if len(aadhaar)!=12:
            return render(request, "VIEWS/form.html", {"error":"Aadhaar number should be of 12 digits"})
            
        if len(occupation)<2 and len(occupation)>128:
            return render(request, "VIEWS/form.html", {"error":"Occupation should  be of length 2 to 128 chars"})
            
        if len(relation)<2 and len(relation)>128:
            return render(request, "VIEWS/form.html", {"error":"Relation should be of length 2 to 128 chars"})

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
        myuser.occupation=occupation            
        myuser.RELATION=relation         
        myuser.accountType=accounttype
        myuser.save()
        return render(request, 'VIEWS/home.html')

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
