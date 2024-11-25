from django.db import models
from django.utils.translation import gettext as _
from users.models import User

from django.utils import timezone

class Restaurant(models.Model):
    class TagChoices(models.TextChoices):
        NEW = 'n'
        LUXURY = 'l'
        DISCOUNT = 'd'
        
    user = models.ForeignKey(User, related_name='restaurants', on_delete=models.CASCADE , blank=True, null=True )
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='restaurants/', blank=True, null=True)
    desc = models.TextField(max_length=5000,blank=True, null=True)
    address = models.TextField(max_length=500,blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    logo = models.ImageField(upload_to='restaurant/logo/',blank=True, null=True)
    min_price = models.FloatField(blank=True, null=True)
    tag = models.CharField(max_length=50 , choices=TagChoices.choices)
    created_at = models.DateTimeField(auto_now_add=False)
    def __str__(self):
        return self.name

class Table(models.Model):
    class TableType(models.TextChoices):
        NORMAL = 'Normal'
        VIB = 'Vib'

    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE , related_name='restaurant_table')
    table_type = models.CharField(max_length=50, choices=TableType.choices , default=TableType.NORMAL)
    number = models.IntegerField(blank=True, null=True) 
    available = models.BooleanField(default=True)
    max_people = models.IntegerField(blank=True, null=True)    

    def __str__(self):
        return f"{self.restaurant.name} - Table {self.number} ({self.table_type})"