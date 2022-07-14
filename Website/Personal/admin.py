from django.contrib import admin
from .models import Signup

admin.site.register(Signup)

class SignupAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','lastname','password','email','phone']

