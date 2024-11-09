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
    restaurant = models.ForeignKey("Restaurant", verbose_name=_(""), on_delete=models.CASCADE)
    table_type = models.FloatField(_(""),blank=True, null=True)
    number = models.IntegerField(_(""),blank=True, null=True) 
    available = models.FloatField(_(""),blank=True, null=True)
    max_people = ''

    def __str__(self):
        return self.restaurant