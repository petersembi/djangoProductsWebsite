from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Log in success')
            return redirect("/freeze/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/accounts/login')
    else: 
        return render(request, 'accounts/login.html')

def register(request):
    # return render (request, 'accounts/register.html')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                # print('username taken')
                messages.info(request, 'Username Taken')
                return redirect('/accounts/register/')

            elif User.objects.filter(email=email).exists():
                # print('email taken')
                messages.info(request, 'Sorry, Email  Taken')
                return redirect('/accounts/register/')

            else:                
                user = User.objects.create_user(username=username, password=password1, email=email, first_name= first_name, last_name=last_name)
                user.save()               
                messages.info(request, 'User  Created Succesfully')
                return redirect('/accounts/login/')
       
        else:
            print('password not matching..')
        return redirect('/accounts/register.html')
    else:
        return render(request, "accounts/register.html")