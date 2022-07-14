from django.db import models

class Signup(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone =models.IntegerField(max_length=100)

    
