from django.urls import path
from . import view

from .views import main, authentication, inventory, usercart, userprofile, userorders, imagesearch

urlpatterns = [
    path('', main.index, name='index'),
    path('login/', authentication.login, name='login'),
    path('register/', authentication.register, name='register'),
    path('logout/', authentication.logout, name='logout'),
    path('floweringplants/', inventory.floweringplants, name='floweringplants'),
    path('seeds/', inventory.seeds, name='seeds'),
    path('gardentools/', inventory.gardentools, name='gardentools'),
    path('uploadImg/', imagesearch.uploadImg, name='uploadImg'),
    path('profile/', userprofile.profile, name='profile'),
    path('cart/', usercart.cart, name='cart'),
    path('confirmorder/', usercart.confirm_order, name='confirmorder'),
    path('userorders/', userorders.userorders, name='userorders'),
    path('addtocart/', usercart.addtocart, name='addtocart'),
    
]

