from django.db import models
from datetime import datetime
# from django.contib.auth.hashers import*
# Create your models here.


class UserDetail(models.Model):
    accountNumber=models.fields.BigIntegerField(14)
    id=models.AutoField(primary_key=True)
    namePrefix=models.fields.CharField(max_length=4, default="Mr.")
    firstName=models.fields.CharField(max_length=50, default="")            
    middleName=models.fields.CharField(max_length=50, default="")           
    lastName=models.fields.CharField(max_length=50, default="")
    username=models.fields.CharField(max_length=128, default="")
    email=models.fields.CharField(max_length=256, default="someone123@gmail.com")
    phoneNumber=models.fields.CharField(max_length=256,default="999_999_999_9")
    alternatePhoneNumber=models.fields.CharField(max_length=256,default=999_999_999_9)           
    address=models.fields.CharField(max_length=256,default="999_999_999_9")            
    motherName=models.fields.CharField(max_length=50, default="")            
    fatherName=models.fields.CharField(max_length=50, default="")         
    zipCode=models.fields.IntegerField(default=800000)            
    dateOfBirth=models.fields.DateField(default="1905-01-01")          
    panNumber=models.fields.CharField(max_length=10, default="AXXXXXXXXX")            
    aadhaarNumber=models.fields.CharField(max_length=12,default="")            
    occupation=models.fields.CharField(max_length=50, default="")
    relation=models.fields.CharField(max_length=50, default="")         
    accountType=models.fields.CharField(max_length=50, default="")
    password=models.fields.CharField(max_length=256,default="")
    

class Account(models.Model):
    accountNumber = models.AutoField(primary_key=True)
    accountUser = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    accountCreationDate = models.fields.DateField(default="1905-01-01")
    accountStatus = models.fields.CharField(max_length=20,default="ACTIVE")
    accountBalance = models.fields.DecimalField(max_digits=20, decimal_places=2)


class Transaction(models.Model):
    transactionId = models.AutoField(primary_key=True)
    fromAccount = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="fromAccountId")
    toAccount = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="toAccountId")
    amount = models.fields.DecimalField(max_digits=20, decimal_places=2)
    transactionDate = models.fields.DateField(default="1905-01-01")
    transactionStatus = models.fields.CharField(max_length=20,default="COMPLETED")
    
class SignupDetails(models.Model):
    
    
    id=models.AutoField(primary_key=True)
    username=models.fields.CharField(max_length=128,default="")
    firstname=models.fields.CharField(max_length=56,default="") 
    lastname=models.fields.CharField(max_length=56,default="")
    email=models.fields.CharField(max_length=156,default="")
    address=models.fields.CharField(max_length=128,default="")
    password=models.fields.CharField(max_length=128,default="")
    phoneNumber=models.fields.CharField(max_length=13,default="")        
   


class CreditRecord(models.Model):
    accountNumber=models.fields.CharField(max_length=16,default="443XXXXXXXXX00")
    amount=models.fields.BigIntegerField()
    dateoftransac.=models.fields.DateField(default="1900-01-01")
    
class DebitRecord(models.Model):
    accountNumber=models.fields.CharField(max_length=16,default="443XXXXXXXXX00")
    amount=models.fields.BigIntegerField()
   
class BankUsers(models.Model):
    id=models.fields.AutoField(primary_key=True)
    username=models.fields.CharField(max_length=10, default="")
    password =models.fields.CharField(max_length=16, default="")