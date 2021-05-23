from django.shortcuts import render, redirect
from django.contrib.auth import models as userModel
from ..models import *

from django.contrib import messages

from .utils import password_check

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = userModel.auth.authenticate(username=username, password=password)

        if user is not None:
            userModel.auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('login')
    else:
        return render(request, "login.html")
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password_check(request,password1):
            if password1 == password2:
                if userModel.User.objects.filter(username=username).exists():
                    messages.info(request, 'Username exists')
                    return redirect('register')
                elif not fname.strip():
                    messages.info(request, 'Firstname cant be blank.')
                    return redirect('register')
                elif len(fname) < 3:
                    messages.info(request, 'Firstname must be atleast 3 characters long.')
                    return redirect('register')
                elif not lname.strip():
                    messages.info(request, 'lastname cant be blank.')
                    return redirect('register')
                elif len(lname) < 3:
                    messages.info(request, 'Lastname must be atleast 3 characters long.')
                    return redirect('register')
                elif not email.strip():
                    messages.info(request, 'email cant be blank.')
                    return redirect('register')
                elif len(email) < 3:
                    messages.info(request, 'email cant be so small.')
                    return redirect('register')
                elif not username.strip():
                    messages.info(request, 'username cant be blank.')
                    return redirect('register')
                elif len(username) < 3:
                    messages.info(request, 'Username must be atleast 3 characters long.')
                    return redirect('register')
                elif userModel.User.objects.filter(email=email).exists():
                    print('email exists')
                    messages.info(request, 'Email exists')
                    return redirect('register')
                else:
                    user = userModel.User.objects.create_user(
                        username=username, email=email, password=password1, first_name=fname, last_name=lname)
                    user.save()
                    return redirect('login')
            else:
                print('pass dosent match')
                messages.info(request, 'Password didn\'t match')
                return redirect('register')
            return redirect('/')
        else:
            return redirect('register')
    else:
        return render(request, "register.html")

def logout(request):
    userModel.auth.logout(request)
    return redirect('/')
