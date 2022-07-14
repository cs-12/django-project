
import email
from django.shortcuts import render,redirect
from .models import Signup




def home(request):
    return render(request,'Personal/home.html')

def signup(request):
     if(request.method=="POST"):
        fn=request.POST.get('txtfirstName','')
        ln=request.POST.get('txtlastName','')
        pwd=request.POST.get('txtPassword','')
        em=request.POST.get('txtEmail','')
        phone=request.POST.get('txtphone','')
        rec=Signup(Firstname=fn,Lastname=ln,password=pwd,email=em,phone=phone)
        rec.save()
        return redirect('signin')
     return render(request,'Personal/signup.html')

  
'''
def signin(request):
    return render(request,'Personal/signin.html')'''


def signin(request):
    response=render(request,'Personal/signin.html')
    if request.method == "POST":
        em=request.POST.get('txtemail')
        pwd=request.POST.get('txtPassword')
        try:
            d1=Signup.objects.get(email=em,password=pwd)
        except Signup.DoesNotExist:
            return render(request,'Personal/signin.html')
        else:  
            request.session['uid'] = d1.id
            return redirect("profile")
    else:
        return render(request,'Personal/signin.html')
def profile(request):
    if(request.session.get('uid')):
        uid=request.session['uid']
        d1=Signup.objects.get(id=uid)
        return render(request,'Personal/profile.html',{'uid':d1})
    else:
        return render(request,'Personal/profile.html')        