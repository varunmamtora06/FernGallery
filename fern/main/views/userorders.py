from django.shortcuts import render, redirect
from ..models import *

def userorders(request):
    ordered_items = None

    try:
        ordered_items = Order.objects.filter(customer=Profile.objects.get(user=request.user)).order_by('-order_date')

    except:
        pass
    
    return render(request, 'userOrders.html', {"ordered_items":ordered_items})
