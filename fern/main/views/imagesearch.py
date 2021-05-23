from django.shortcuts import render, redirect
from django.contrib import messages

from ..models import *
from django.core.exceptions import ObjectDoesNotExist
from decouple import config
from ..create_labels import *

from keras.preprocessing.image import img_to_array , load_img
from keras.models import load_model
import numpy as np

import base64
from .utils import show_recent_file


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



