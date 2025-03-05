from django.db import models

from users.models import User
from meals.models import Meals
from booking.models import Coupon

class Cart(models.Model):

    user = models.ForeignKey(User , related_name='cart_user' , on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon , related_name='cart_coupon', on_delete=models.CASCADE , blank=True, null=True)
    total_after_coupon = models.FloatField(blank=True, null=True)
    total = models.FloatField()

    def __str__(self):
        return str(self.user)

def cart_total(self):
    return round(sum(item.total or 0 for item in self.cart_detail.all()), 2)

class MealsDetail(models.Model):
    cart = models.ForeignKey(Cart , related_name='cart_detail' , on_delete=models.CASCADE)
    meal = models.ForeignKey(Meals , related_name='cart_meals', on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(default=0)
    total = models.FloatField(blank=True, null=True , default=0)

    def __str__(self):
        return str(self.cart)


class Order(models.Model):
    cart = models.ForeignKey(Cart , related_name='order_cart',on_delete=models.CASCADE)
    meals_detail = models.ForeignKey(MealsDetail , related_name='meals_detail_order', on_delete=models.CASCADE)
    coupon_id = models.ForeignKey(Coupon , on_delete=models.CASCADE , blank=True, null=True)
    code = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50)
    total_price = models.IntegerField(max_length=50)
    payment_status = models.CharField(max_length=50)
    total_after_coupon = models.FloatField()
    created_at = models.TimeField(auto_now=True)
    delivery_time = models.TimeField()
    delivery_location = models.CharField(max_length=50 , blank=True, null=True)
    

    def __str__(self):
        return str(self.cart)