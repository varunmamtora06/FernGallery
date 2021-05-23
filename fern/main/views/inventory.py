from django.shortcuts import render, redirect
from ..models import *

def floweringplants(request):

    floweringplants = Item.objects.filter(category="floweringplants").exclude(item_count__lte=0)
    
    if request.method == "POST":
        item = request.POST["item"]
        remove = None
        try:
            remove = request.POST["remove"]
        except:
            pass
        print(item)
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(item)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(item)
                    else:
                        print("remove1 ",remove)
                        cart[item]  = quantity-1
                else:
                    print("remove ",remove)
                    print("sessI: ", request.session)
                    cart[item]  = quantity+1

            else:
                cart[item] = 1
        else:
            cart = {}
            cart[item] = 1

        request.session['cart'] = cart
        print("sessI: ", request.session.keys())
        print('cart' , request.session['cart'])
        return render(request, 'floweringplants.html', {"items":floweringplants})
        
    return render(request, 'floweringplants.html',{"items":floweringplants})

def seeds(request):

    seeds = Item.objects.filter(category="seeds").exclude(item_count__lte=0)
    
    if request.method == "POST":
        item = request.POST["item"]
        remove = None
        try:
            remove = request.POST["remove"]
        except:
            pass
        print(item)
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(item)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(item)
                    else:
                        print("remove1 ",remove)
                        cart[item]  = quantity-1
                else:
                    print("remove ",remove)
                    print("sessI: ", request.session)
                    cart[item]  = quantity+1

            else:
                cart[item] = 1
        else:
            cart = {}
            cart[item] = 1

        request.session['cart'] = cart
        print("sessI: ", request.session.keys())
        print('cart' , request.session['cart'])
        return render(request, 'seeds.html', {"items":seeds})
        
    return render(request, 'seeds.html',{"items":seeds})

def gardentools(request):

    gardentools = Item.objects.filter(category="gardentools").exclude(item_count__lte=0)
    
    if request.method == "POST":
        item = request.POST["item"]
        remove = None
        try:
            remove = request.POST["remove"]
        except:
            pass
        print(item)
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(item)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(item)
                    else:
                        print("remove1 ",remove)
                        cart[item]  = quantity-1
                else:
                    print("remove ",remove)
                    print("sessI: ", request.session)
                    cart[item]  = quantity+1

            else:
                cart[item] = 1
        else:
            cart = {}
            cart[item] = 1

        request.session['cart'] = cart
        print("sessI: ", request.session.keys())
        print('cart' , request.session['cart'])
        return render(request, 'gardentools.html', {"items":gardentools})
        
    return render(request, 'gardentools.html',{"items":gardentools})
