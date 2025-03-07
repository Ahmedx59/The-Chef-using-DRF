from django.db import models

from users.models import User
from meals.models import Meals
from booking.models import Coupon

class Cart(models.Model):

    user = models.ForeignKey(User , related_name='cart_user' , on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon , related_name='cart_coupon', on_delete=models.CASCADE , blank=True, null=True)
    total_after_coupon = models.FloatField(blank=True, null=True)
    total = models.FloatField(default=0,blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def cart_total(self):
        return round(sum(item.total or 0 for item in self.cart_item.all()), 2)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart , related_name='cart_item' , on_delete=models.CASCADE)
    meal = models.ForeignKey(Meals , related_name='cart_item', on_delete=models.SET_NULL , blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(default=0)
    total = models.FloatField(blank=True, null=True , default=0)

    def __str__(self):
        return str(self.cart)


class Order(models.Model):
    user = models.ForeignKey(User , related_name='order' , on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50)
    total_price = models.IntegerField(max_length=50)
    payment_status = models.CharField(max_length=50)
    coupon = models.ForeignKey(Coupon ,on_delete=models.SET_NULL ,related_name="order", blank=True, null=True)
    total_after_coupon = models.FloatField(blank=True, null=True)
    created_at = models.TimeField(auto_now=True)
    delivery_time = models.TimeField()
    delivery_location = models.CharField(max_length=50 , blank=True, null=True)

    def __str__(self):
        return str(self.cart)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='order_item', on_delete=models.CASCADE)
    meal = models.ForeignKey(Meals , related_name='order_item',on_delete=models.SET_NULL , blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(default=0)
    total = models.FloatField(blank=True, null=True , default=0)
