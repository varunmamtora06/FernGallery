from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.exceptions import ObjectDoesNotExist

from ..models import *

def profile(request):
    
    if request.method == 'POST':
        Profile.objects.create(phone=request.POST['contact'], address=request.POST['address'], user=request.user)
        return redirect('profile')

    else:
        profile = None

        try:
            profile = Profile.objects.get(user=request.user)
        except ObjectDoesNotExist:
            messages.info(request,'Your profile dosent exist.')
    
    return render(request,'profile.html',{"profile":profile})    
