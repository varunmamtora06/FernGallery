from django.shortcuts import render, redirect
from ..models import *

from .utils import order_mail

def addtocart(request):
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

        return redirect('cart')

def cart(request):

    if request.method == 'POST':
        cart = request.session['cart']
        item = request.POST['item']
        remove = None
        print("newcart",cart)
        print("newitem",item)
        try:
            remove = request.POST['remove']
        except:
            pass
        
        quantity = cart.get(item)
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
            print("{} qunt is {}".format(item, cart[item]))
        
        request.session['cart'] = cart
        return redirect('cart')
    else:
        return render(request, 'cart.html')

def confirm_order(request):
    cart = request.session['cart']
    total = 0
    order_success = 0

    for item_id, quantity in cart.items():
        item = Item.objects.get(id=item_id)
        total += item.item_price * quantity
        item.item_count -= quantity
        order = Order(customer = Profile.objects.get(user=request.user), ordered_item = item, order_quantity = quantity, total_order_amount = total)
        print("phatka: ", total)
        order.save()
        item.save()
        order_success = 1
        
    
    if order_success == 1:
        order_mail(request, total)
        del request.session['cart']
        return redirect('cart')
    else:
        pass