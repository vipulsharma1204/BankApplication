from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
from home.models import UserDetail, Transaction, Account,SignupDetails,BankUsers,CreditRecord,DebitRecord
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from decimal import Decimal
import json
import re
import random,string
from datetime import datetime

def log(data):
    open("logging.txt","a").write(str(datetime.now())+"\t"+str(data)+"\n")

def jsonParse(cbody):
    return json.loads(cbody)

def login(request):
    print(request.POST)
    if request.method=="GET":
        return render(request, 'VIEWS/login.html', {"":""} )
    if request.method=="POST":
        username=request.POST.get('userName',"")
        password=request.POST.get('password',"")
                
        if SignupDetails.objects.filter(username=username):
            
            searchResult = SignupDetails.objects.get(username=username)
                       
            
            if searchResult:
                
                flag=check_password(password,searchResult.password)
                
                if flag:
                    return render(request, 'VIEWS/form.html',{"userData":searchResult})
                else:
                    return render(request, 'VIEWS/login.html',{"error":"Password or Email is Invalid"})
                    
                    
            else:
                return render(request, 'VIEWS/login.html',{"error":"Password or Email is Invalid"})
                
    return render(request, 'VIEWS/login.html', {'error':'Couldn\'t login'})

def searchDetails(request):
    if request.method=="GET":
        return render(request, 'VIEWS/searchDetails.html', {"isPresent":False})
    
    if request.method=="POST":
        searchby=request.POST.get('searchby',"")
        details=request.POST.get('details',"")
        searchResult = []
        if searchby=="name":            
            searchResult = UserDetail.objects.filter(firstName=details).union(
                UserDetail.objects.filter(lastName=details)
            ).union(
                UserDetail.objects.filter(middleName=details)
            )
            
        elif searchby=="phoneNumber":            
            searchResult = UserDetail.objects.filter(phoneNumber=details).union(
                UserDetail.objects.filter(alternatePhoneNumber=details)
            )
            
        elif searchby=="panNumber":            
            searchResult = UserDetail.objects.filter(panNumber=details)
            
        elif searchby=="aadhaarNumber":            
            searchResult = UserDetail.objects.filter(aadhaarNumber=details)
            
        elif searchby=="accountNumber":
            searchResult=UserDetail.objects.filter(accountNumber=details)
            
        
        print("Data :"+str(searchResult))
        return render(request, 'VIEWS/searchDetails.html', {"searchDetails": searchResult, "isPresent":True})
                

def home(request):
    return render(request, 'VIEWS/home.html',{"":""})

def form(request):
    accno=random.randint(100000000000,900000000000)
    
    # this is for GET method
    if request.method=="GET":
        return render(request, 'VIEWS/form.html',{"userData":SignupDetails.objects.all()[0]})

    
    # this is for POST method
    if request.method=='POST':
        userObject = jsonParse(request.body)
        log(userObject)
        if not UserDetail.objects.filter(accountNumber=accno).exists():
            accountNumber=accno
            print(accountNumber)
        else:
            accno=random.randint(100000000000,900000000000)
                

        namePrefix=userObject['namePrefix']   
        fname=userObject['firstName']
        mname=userObject['middleName']
        lname=userObject['lastName']
        email=userObject['email']
        username=userObject['username']
        contact=userObject['contact']
        alternatenumber=userObject['alternateNumber']        
        address=userObject['address']
        mothername=userObject['motherName']
        fatherName=userObject['fatherName']
        pincode=userObject['zipCode']
        dob=userObject['dob']
        PAN=userObject['panNumber']
        aadhaar=userObject['aadhaarNumber']
        occupation=userObject['occupation']
        relation=userObject['relation']
        accounttype=userObject['MemberType']
    

        if not UserDetail.objects.filter(panNumber=PAN).exists():
            print("new pan number")
        else:
            return render(request, "VIEWS/form.html", {"error":"PAN Number you have entered is already exist."})
        
        if not UserDetail.objects.filter(aadhaarNumber=aadhaar).exists():
            print("new aadhaar number entered")
        else:
            return render(request, "VIEWS/form.html", {"error":"Aadhar Number you have entered already exist."})
            
        if not UserDetail.objects.filter(email=email).exists():
            print("new id found")     
        else:
            pass      
            
        
            
        myuser = UserDetail()
        myuser.accountNumber=accountNumber     
        myuser.namePrefix=namePrefix    
        myuser.firstName=fname            
        myuser.middleName=mname           
        myuser.lastName=lname
        myuser.email=email
        myuser.username=username
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
        return render(request,'VIEWS/login.html',{"":""})

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
        
        
        if not UserDetail.objects.filter(email=email).exists():
            print("hello")
        else:
            
            return render(request, "VIEWS/Signup.html", {"error":"Email Id already exists."})
            
        if not UserDetail.objects.filter(phoneNumber=contact):
            print("new contact found\n")
        else:
            return render(request, "VIEWS/Signup.html", {"error":"Contact already exist."})
          
        if not UserDetail.objects.filter(username=username).exists():
            if not username.isalnum():
                return render(request, "VIEWS/Signup.html", {"error":"your username must contains only chars and digits"})
        else:
            return render(request, "VIEWS/Signup.html", {"error":"Username that you have choosen is already exist."})
                                                         
        if len(address)>200:
            return render(request, "VIEWS/Signup.html", {"error":"Max 200 chars allowed in address"})
            
        if password!=password1:
            return render(request, "VIEWS/Signup.html", {"error":"Password mismatch"})
        
        elif len(password)<=8 or len(password)>=64:
            return render(request, "VIEWS/Signup.html", {"error":"Password length should be between 8 to 64 chars"})
        
        myuser=SignupDetails()
        myuser.username=username
        myuser.firstname=fname
        myuser.lastname=lname
        myuser.email=email
        myuser.address=address
        myuser.password=make_password(password)
        myuser.phoneNumber=contact
        myuser.save()
        return render(request, "VIEWS/login.html", {"error":""})
    
    return redirect(login)

def showUsers(request):
    
    return render(request, 'VIEWS/users.html', {"users": UserDetail.objects.all()})

def manageTransactions(request):
    if request.method=="GET":
        return render(request, "VIEWS/transactions.html", {
            "allTransactions":Transaction.objects.all(),
            "allAccounts" : Account.objects.all()
        })
    elif request.method=="POST":
        fromAccount = Account.objects.filter(accountNumber=request.POST.get("fromAccount"))[0]
        toAccount = Account.objects.filter(accountNumber=request.POST.get("toAccount"))[0]
        transaction = Transaction()
        transaction.transactionDate = datetime.today()
        transaction.fromAccount = fromAccount
        transaction.toAccount = toAccount
        transaction.amount = request.POST.get("amount")
        fromAccount.accountBalance -= Decimal(transaction.amount)
        toAccount.accountBalance += Decimal(transaction.amount)

        if fromAccount==toAccount:
            return render(request, "VIEWS/transactions.html", {
                "allTransactions": Transaction.objects.all(),
                "allAccounts": Account.objects.all(),
                "errorMessage": "From and to accounts can't be same"
            })
        transaction.save()
        fromAccount.save()
        toAccount.save()
        print(transaction)
        return render(request, "VIEWS/transactions.html", {
            "allTransactions":Transaction.objects.all(),
            "allAccounts" : Account.objects.all()
        })



def identify(request):
    if request.method=="GET":
        return render(request, "VIEWS/identification.html",{"":""})
    if request.method=="POST":
        username=request.POST.get("userName","")
        password=request.POST.get("password","")
        if BankUsers.objects.filter(username=username, password=password).exists():
            return render(request,"VIEWS/home.html",{"error":"Id or Password is incorrect"})

        else:
            return render(request,"VIEWS/identification.html",{"error":"Id or Password is incorrect"})
                
    else:
        return render(request, "VIEWS/identifiation.html", {"error":"Id or Password is incorrect"})



def adduser(request):
    return render(request, 'VIEWS/form.html',{"":""})
def transaction(request):
    if request.method=="GET":
        return render(request,'VIEWS/transactions.html',{"":""})
def help(request):
    return render(request, 'VIEWS/help.html', {"":""})

def update(request):
    if request.method=="GET":
        return render(request, 'VIEWS/update.html',{"":""})
    if request.method=="POST":
        accountNumber=request.POST.get('account',"")
        phoneNumber=request.POST.get('phone',"")
        print(accountNumber,"\t",phoneNumber)
        
        if UserDetail.objects.filter(accountNumber=accountNumber, phoneNumber=phoneNumber).exists():
            details=UserDetail.objects.get(accountNumber=accountNumber, phoneNumber=phoneNumber)
            log("sending details"+str(details))
            details.dateOfBirth = str(datetime.strptime(str(details.dateOfBirth), "%Y-%m-%d %H:%M:%S"))
            return render(request, 'VIEWS/update.html', {"userData": details, "isPresent":True})
        
        else:
            return render(request, 'VIEWS/update.html',{"error":"Account Number or Password is incorrect"})

def credit(request):
    if request.method=="GET":
        return render(request, 'VIEWS/credit.html',{"":""})
    if request.method=="POST":
        
        accountNumber=request.POST.get('accountNumber',"")
        amount=request.POST.get('amount',"")
        if UserDetail.objects.filter(accountNumber=accountNumber).exists():
            myuser=CreditRecord
            myuser.accountNumber=accountNumber
            myuser.amount=amount
            myuser.dateoftransac=datetime.today()
            myuser.save()
            return render(request, 'VIEWS/credit.html',{"":""})
        else:
            return render(request,'VIEWS/credit.html',{"error":"account not found"})
    else:
        return render(request,'VIEWS/credit.html',{"error":"something went wrong!"})
            
            
        
        
def debit(request):
    if request.method=="GET":
        return render(request, 'VIEWS/debit.html',{"":""})
    if request.method=="POST":
        accountNumber=request.POST.get('accountNumber',"")
        amount=request.POST.get('amount',"")
        if UserDetail.objects.filter(accountNumber=accountNumber).exists():
            myuser=DebitRecord
            myuser.accountNumber=accountNumber
            myuser.amount=amount
            myuser.dateoftransac=datetime.today()
            myuser.save()
            return render(request, 'VIEWS/debit.html',{"":""})
        else:
            return render(request,'VIEWS/debit.html',{"error":"account not found"})
    else:
        return render(request,'VIEWS/debit.html',{"error":"something went wrong!"})
        
     
            
def updateUserDetails(request):
    userObject = jsonParse(request.body)
    log(userObject)
    if request.method=="POST":
            
        namePrefix=userObject['namePrefix']  
        accountNumber=userObject['accountNumber'] 
        fname=userObject['firstName']
        mname=userObject['middleName']
        lname=userObject['lastName']
        email=userObject['email']
        username=userObject['username']
        contact=userObject['contact']
        alternatenumber=userObject['alternateNumber']        
        address=userObject['address']
        mothername=userObject['motherName']
        fatherName=userObject['fatherName']
        pincode=userObject['zipCode']
        dob=userObject['dob']
        PAN=userObject['panNumber']
        aadhaar=userObject['aadhaarNumber']
        occupation=userObject['occupation']
        relation=userObject['relation']
        accounttype=userObject['MemberType']
        
        myuser=UserDetail.objects.get(accountNumber=accountNumber)
        myuser.namePrefix=namePrefix
        myuser.firstName=fname
        myuser.middleName=mname
        myuser.lastName=lname
        myuser.email=email
        myuser.username=username
        myuser.phoneNumber=contact
        myuser.alternatePhoneNumber=alternatenumber
        myuser.address=address
        myuser.motherName=mothername
        myuser.fatherName=fatherName
        myuser.zipCode=pincode
        myuser.dateOfBirth=dob[:10]
        myuser.panNumber=PAN
        myuser.aadhaarNumber=aadhaar
        myuser.occupation=occupation
        myuser.relation=relation
        myuser.accountType=accounttype
        myuser.save()
        return render(request, 'VIEWS/update.html', {"":""})