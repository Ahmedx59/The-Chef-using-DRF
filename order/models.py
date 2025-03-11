from django.db import models

from users.models import User
from meals.models import Meals
from booking.models import Coupon

class Cart(models.Model):

    user = models.OneToOneField(User , related_name="cart", on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon , related_name='cart_coupon', on_delete=models.CASCADE , blank=True, null=True)
    total_after_coupon = models.FloatField(blank=True, null=True)
    total = models.FloatField(default=0,blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def save(self,*args, **kwargs):
        self.total = self.cart_total()
        return super().save(*args, **kwargs)
    
    def cart_total(self):
        return round(sum(item.total for item in self.cart_item.all()), 2)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart , related_name='cart_item' , on_delete=models.CASCADE)
    meal = models.ForeignKey(Meals , related_name='cart_item', on_delete=models.SET_NULL , blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(default=0)
    total = models.FloatField(blank=True, null=True , default=0)

    def __str__(self):
        return str(self.cart)


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        RECEIVED ='Received'
        PROCESSED = 'Processed'
        SHIPPED = 'Shipped'
        DELIVERED = 'Delivered'

    user = models.ForeignKey(User , related_name='order' , on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50 , choices=OrderStatus.choices , default=OrderStatus.RECEIVED)
    total_price = models.IntegerField(max_length=50,blank=True, null=True)

    is_paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon ,on_delete=models.SET_NULL ,related_name="order", blank=True, null=True)
    total_after_coupon = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_time = models.DateTimeField()
    delivery_location = models.CharField(max_length=50 , blank=True, null=True)

    def __str__(self):
        return str(self.user)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='order_item', on_delete=models.CASCADE)
    meal = models.ForeignKey(Meals , related_name='order_item',on_delete=models.SET_NULL , blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(default=0)
    total = models.FloatField(blank=True, null=True , default=0)
