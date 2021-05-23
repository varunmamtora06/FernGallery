import glob
import os.path

from django.core.mail import send_mail
from decouple import config
import datetime

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

def show_recent_file(fileName):

    folder_path = "../fern/identifImgs/*"
    files = glob.glob(folder_path)
    max_file = max(files, key=os.path.getctime)

    # print (max_file[36:])
    return max_file[20:]

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
        config('EMAIL_HOST_USER'),
        [request.user.email],
        fail_silently=False,
        )
    print("email sent")