from django.db import models
# Create your models here.


class UserDetail(models.Model):
    namePrefix=models.fields.CharField(max_length=4, default="Mr.")
    firstName=models.fields.CharField(max_length=50, default="")            
    middleName=models.fields.CharField(max_length=50, default="")           
    lastName=models.fields.CharField(max_length=50, default="")
    username=models.fields.CharField(max_length=128, default="")
    email=models.fields.CharField(max_length=256, default="someone123@gmail.com")
    phoneNumber=models.fields.BigIntegerField(default=999_999_999_9)
    alternatePhoneNumber=models.fields.BigIntegerField(default=999_999_999_9)           
    address=models.fields.CharField(max_length=256,default="999_999_999_9")            
    motherName=models.fields.CharField(max_length=50, default="")            
    fatherName=models.fields.CharField(max_length=50, default="")         
    zipCode=models.fields.IntegerField(default=800000)            
    dateOfBirth=models.fields.DateField(default="1905-01-01")          
    panNumber=models.fields.CharField(max_length=10, default="AXXXXXXXXX")            
    aadhaarNumber=models.fields.BigIntegerField(default="999_999_999_999")            
    occupation=models.fields.CharField(max_length=50, default="")
    relation=models.fields.CharField(max_length=50, default="")         
    accountType=models.fields.CharField(max_length=50, default="")


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
