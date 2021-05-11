from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('floweringplants/', views.floweringplants, name='floweringplants'),
    path('seeds/', views.seeds, name='seeds'),
    path('gardentools/', views.gardentools, name='gardentools'),
    path('uploadImg/', views.uploadImg, name='uploadImg'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
    path('confirmorder/', views.confirm_order, name='confirmorder'),
    path('userorders/', views.userorders, name='userorders'),
    path('addtocart/', views.addtocart, name='addtocart'),
    # path('updateDB/', views.updateDB, name='updateDB'),
]
