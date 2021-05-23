from django.shortcuts import render, redirect
from ..models import *

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'profile.html',{"profile":profile})    
