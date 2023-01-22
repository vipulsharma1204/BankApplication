from django.contrib import admin

# Register your models here.
from .models import UserDetail
from .models import SignupDetails
from .models import BankUsers

admin.site.register(UserDetail)
admin.site.register(SignupDetails)
admin.site.register(BankUsers)

