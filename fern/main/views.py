from django.shortcuts import render, redirect
from django.contrib.auth import models as userModel
from django.contrib import messages
import datetime

from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from .create_labels import *
from keras.preprocessing.image import img_to_array , load_img
from keras.models import load_model
import numpy as np
from keras.preprocessing.image import img_to_array , load_img
from keras.models import load_model


def index(request):
    return render(request, 'index.html')

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

def password_check(request, passwd): 
    SpecialSym =['$', '@', '#', '%'] 
    val = True
    msg = ""
    if len(passwd) < 6:
        val = False
        msg="length should be at least 6"
        messages.info(request, msg)
        

    if not any(char.isdigit() for char in passwd): 
        val = False
        msg="Password should have at least one numeral"
        messages.info(request, msg)

    if not any(char.isupper() for char in passwd): 
        val = False
        msg="Password should have at least one uppercase letter"
        messages.info(request, msg)

    if not any(char.islower() for char in passwd): 
        val = False
        msg="Password should have at least one lowercase letter"
        messages.info(request, msg)

    if not any(char in SpecialSym for char in passwd): 
        val = False
        msg="Password should have at least one of the symbols $@#%"
        messages.info(request, msg)

    return val

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

def showRecentFile(fileName):
    import glob
    import os.path

    folder_path = "../fern/identifImgs/*"
    files = glob.glob(folder_path)
    max_file = max(files, key=os.path.getctime)

    # print (max_file[36:])
    return max_file[20:]

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

import base64
def uploadImg(request):
    if request.method == 'POST':
        img = request.FILES.get('pic')
        fileName = str(img)
        img_en = base64.b64encode(img.read())
        with open("../fern/identifImgs/"+fileName, "wb") as fh:
            fh.write(base64.b64decode(img_en))
        print(showRecentFile(fileName))

        recent_file = showRecentFile(fileName)
        print(recent_file)


        model = load_model('../fern/main/Flowers_CLeared.h5')

        img = load_img("../fern/identifImgs/"+recent_file, target_size = (150,150))
        img = img_to_array(img)
        img = np.expand_dims(img , axis = 0)


        test_o = model.predict(img)
        test_1 = np.argmax(test_o,axis=1)

        
        print(get_label(test_1))
        output = get_label(test_1)[0]

        item = None

        try:
            item = Item.objects.get(item_name = output)
        except ObjectDoesNotExist:
            item = None
            messages.info(request, 'Sorry we don\'t have this item yet')

        print("item iz: ",item)
        context = {
            "item":item,
        }
        return render(request,'tp.html',context)

    else:
        return render(request, 'tp.html')
    return render(request, 'tp.html')


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'profile.html',{"profile":profile})    

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

def order_mail(request, total=0):
    orders = Order.objects.filter(customer=Profile.objects.get(user=request.user)).filter(order_date=datetime.date.today())

    print(f"total:{total}")

    body = "You ordered\n"
    orders = list(set(orders))
    print(orders)
    for order in orders:
        # body = body + order.ordered_item.item_name + "\n"
        body += f"{order.ordered_item.item_name} X {order.order_quantity} pcs \n"

    body += f"Total is: {total} Rs."
    
    send_mail(
        'Order Confirmed.',
        body,
        'varunmamtora@gmail.com',
        [request.user.email],
        fail_silently=False,
        )
    print("email sent")


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

def userorders(request):
    ordered_items = None

    try:
        ordered_items = Order.objects.filter(customer=Profile.objects.get(user=request.user)).order_by('-order_date')

    except:
        pass
    
    return render(request, 'userOrders.html', {"ordered_items":ordered_items})


# def updateDB(request):
    
#     Item.objects.create(item_name='rose',item_details='Rose Flowering Plant',item_review='',category='floweringplants',item_price=499,item_count=30,item_image='C:/Users/varun/mpr/fern/media/itemImages/Rose3.jpg')
