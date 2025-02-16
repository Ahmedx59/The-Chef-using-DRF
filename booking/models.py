from django.db import models


from users.models import User
from restaurant.models import Table , Restaurant

class Booking(models.Model):
    class BookingStatus(models.TextChoices):
        ACTIVE = 'active'
        ENDED = 'ended'
        CANCELED = 'canceled'  

    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='booking')
    restaurant = models.ForeignKey(Restaurant ,on_delete=models.CASCADE , related_name='booking', blank=True, null=True)
    table = models.ForeignKey(Table ,on_delete = models.SET_NULL , related_name='booking' , null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50 , choices=BookingStatus.choices, default=BookingStatus.ACTIVE, blank=True, null=True)
    code = models.CharField(max_length=50,blank=True, null=True)
    coupon = models.ForeignKey("Coupon", on_delete=models.SET_NULL , related_name='booking',blank=True, null=True) 
    


class Coupon(models.Model): 
    code = models.CharField(max_length=50)
    quantity = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    discount = models.DecimalField(max_digits=3, decimal_places=1) 
