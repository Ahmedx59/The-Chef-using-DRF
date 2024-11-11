from django.db import models
from django.utils.translation import gettext as _


class Restaurant(models.Model):
    email = models.EmailField(_(""), max_length=254)
    name = models.CharField(_(""), max_length=50,)
    image = models.ImageField(_(""), upload_to='restaurants/', blank=True, null=True)
    desc = models.TextField(_(""), max_length=5000,blank=True, null=True)
    address = models.TextField(_(""),max_length=500,blank=True, null=True)
    phone = models.IntegerField(_("") ,blank=True, null=True)
    logo = models.ImageField(_(""), upload_to='restaurant/logo/',blank=True, null=True)
    min_price = models.FloatField(_(""),blank=True, null=True)
    tag = ''

    def __str__(self):
        return self.name

class Table(models.Model):
    class TableType(models.TextChoices):
        NORMAL = 'Normal'
        VIB = 'Vib'

    class TableAvailable(models.TextChoices):
        AVAILABLE = 'Available'
        RESERVED = 'Reserved'

    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE , related_name='restaurant_table')
    table_type = models.CharField(_(""), max_length=50, choices=TableType.choices , default=TableType.NORMAL)
    number = models.IntegerField(_(""),blank=True, null=True) 
    available = models.CharField(_(""), max_length=50 , choices=TableAvailable.choices , default=TableAvailable.RESERVED)
    max_people = models.IntegerField(_(""),blank=True, null=True)

    # def __str__(self):
    #     return self.restaurant
    

    def __str__(self):
        # Return the restaurant name and table type for clarity
        return f"{self.restaurant.name} - Table {self.number} ({self.table_type})"