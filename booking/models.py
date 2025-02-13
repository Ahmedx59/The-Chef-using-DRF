from django.db import models


from users.models import User
from restaurant.models import Table 

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='booking')
    table = models.ManyToManyField(Table , related_name='booking')
    code = models.CharField(max_length=50)
    booking_date = models.DateTimeField() 
