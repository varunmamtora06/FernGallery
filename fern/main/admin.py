from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['id','address','phone','user']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=['id','item_name','category','item_price','item_count']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','customer','ordered_item','order_date']