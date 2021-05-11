from django.db import models
from django.contrib.auth import models as mod
# Create your models here.

class Profile(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=11)
    user = models.OneToOneField(mod.User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Item(models.Model):
    CATEGORIES = (
        ('floweringplants','floweringplants'),
        ('seeds','seeds'),
        ('gardentools','gardentools'),
    )
    item_name = models.CharField(max_length=150)
    item_details = models.CharField(max_length=300)
    item_review = models.CharField(max_length=250, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORIES)
    item_price = models.IntegerField()
    item_count = models.IntegerField()
    item_image = models.ImageField(upload_to="itemImages/", blank=True)

    def __str__(self):
        return self.item_name
    

class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ordered_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order_quantity = models.IntegerField(null = True)
    total_order_amount = models.IntegerField(null = True)
    order_date = models.DateField(auto_now_add=True, blank=True)
    is_delivered = models.BooleanField(default=False)

    def is_item_delivered(self):
        if self.is_delivered:
            return "Delivered"
        else:
            return "Not Delivered"
    
    def item_amount(self):
        '''returns total amount for a particular item in order'''
        return self.order_quantity * self.ordered_item.item_price
    


