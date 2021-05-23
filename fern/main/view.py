from django.shortcuts import render, redirect
from django.contrib.auth import models as userModel
from django.contrib import messages
import datetime

from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from decouple import config
from .create_labels import *
from keras.preprocessing.image import img_to_array , load_img
from keras.models import load_model
import numpy as np
from keras.preprocessing.image import img_to_array , load_img
from keras.models import load_model


import base64
from .views.utils import show_recent_file


def uploadImg(request):
    if request.method == 'POST':
        img = request.FILES.get('pic')
        fileName = str(img)
        img_en = base64.b64encode(img.read())
        with open("../fern/identifImgs/"+fileName, "wb") as fh:
            fh.write(base64.b64decode(img_en))
        print(show_recent_file(fileName))

        recent_file = show_recent_file(fileName)
        print(recent_file)


        model = load_model('../fern/main/Flowers_CLeared.h5')

        img = load_img("../fern/identifImgs/"+recent_file, target_size = (150,150))
        img = img_to_array(img)
        img = np.expand_dims(img , axis = 0)


        test_o = model.predict(img)
        test_1 = np.argmax(test_o,axis=1)

        
        print(get_label(test_1))
        output = get_label(test_1)[0]

        os.remove(f'../fern/identifImgs/{recent_file}')

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



def userorders(request):
    ordered_items = None

    try:
        ordered_items = Order.objects.filter(customer=Profile.objects.get(user=request.user)).order_by('-order_date')

    except:
        pass
    
    return render(request, 'userOrders.html', {"ordered_items":ordered_items})


# def updateDB(request):
    
#     Item.objects.create(item_name='rose',item_details='Rose Flowering Plant',item_review='',category='floweringplants',item_price=499,item_count=30,item_image='C:/Users/varun/mpr/fern/media/itemImages/Rose3.jpg')
