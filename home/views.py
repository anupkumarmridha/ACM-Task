from django.db import models
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from datetime import datetime
#import re
from home.EmailBackEnd import EmailBackEnd
from home.models import Contact,Post

# Create your views here.
def home(request):
    return render(request,'home/home.html')
def blog(request):
    return render(request,'home/blog.html')
def contact(request):
    return render(request,'home/contact.html')
def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request, "Please fill the from correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc, timeStamp=datetime.today())
            contact.save()
            messages.success(request, 'Your Massage has been sent!.')
    return render(request, 'home/contact.html')

def handleLogin(request):
    if request.method != 'POST':
        return HttpResponse('Submission outside this window is not allowed 😎')
    else:
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user =EmailBackEnd.authenticate(request, username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request,"Successfuly logged in 🥰")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials, please try again 😎")
            return redirect('home')
    
def handleLogout(request):
        logout(request)
        messages.success(request,"successfully logout 🥰")
        return redirect('home')      

def handelSingup(request):
    if request.method =='POST':
        #Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        #phonenumber = request.POST['phonenumber']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check for errorneous input
        """
        #username
        if len(username) > 25:
            messages.error(request, "username is too long(must be less than 26 character)")
            return redirect('signup')
        if len(username) < 3:
            messages.error(request, "'username is short(must be more than 2 character)")
            return redirect('signup')
            #password
        if len(pass1) < 8:
            messages.error(request, "Make sure your password is at lest 8 characters")
            return redirect('signup')
        if len(pass1) > 20:
            messages.error(request, "Make sure your password is under 20 characters")
            return redirect('signup')
            #pass1 & pass2 should be same
        """
        if pass1 != pass2 :
            messages.error(request, "Password do not match.")
            return redirect('handelSingup')
        #Create User
        try:
            myuser = User.objects.create_user(username=username, email=email,password=pass1)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            messages.success(request, "your ACM account has been successfully created 🥰")
            return redirect('home')
        except:
            messages.error(request, "Failed to SignUp!")
            return redirect('home')
