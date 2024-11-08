from django.db import models
from django.utils.translation import gettext as _


class Restaurant(models.Model):
    email = models.EmailField(_(""), max_length=254)
    name = models.CharField(_(""), max_length=50)
    image = models.ImageField(_(""), upload_to='restaurants/', blank=True, null=True)
    desc = models.TextField(_(""), max_length=5000)
    address = models.TextField(_(""),max_length=500)
    phone = models.IntegerField(_("") )
    logo = models.ImageField(_(""), upload_to='restaurant/logo/')
    min_price = models.FloatField(_(""))
    tag = ''



class Table(models.Model):
    restaurant = models.ForeignKey("Restaurant", verbose_name=_(""), on_delete=models.CASCADE)
    table_type = models.FloatField(_(""))
    number = models.IntegerField(_("")) 
    available = models.FloatField(_(""))
    max_people = ''