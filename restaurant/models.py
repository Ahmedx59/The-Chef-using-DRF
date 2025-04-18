from django.db import models

from django.utils.translation import gettext as _

from django.utils import timezone

from django.dispatch import receiver
from django.db.models.signals import post_save

from users.models import User


class Restaurant(models.Model):
    class TagChoices(models.TextChoices):
        NEW = 'n'
        LUXURY = 'l'
        DISCOUNT = 'd'
        
    user = models.ForeignKey(User, related_name='restaurants', on_delete=models.CASCADE , blank=True, null=True )
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='restaurants/', blank=True, null=True)
    desc = models.TextField(max_length=5000,blank=True)
    address = models.TextField(max_length=500,blank=True)
    phone = models.CharField(max_length=50,blank=True, null=True)
    logo = models.ImageField(upload_to='restaurant/logo/',blank=True, null=True)
    min_price = models.FloatField(blank=True, null=True)
    tag = models.CharField(max_length=50 , choices=TagChoices.choices )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE , related_name='restaurant_table')
    title = models.CharField(max_length=50,blank=True, null=True)
    extra_price = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    


@receiver(post_save, sender=User)
def owner(instance , created , *args, **kwargs):
    if created:
        if instance.user_type == User.UserType.SELLER:
            Restaurant.objects.create(
                user = instance,
                name = instance.email,
                email = instance.email
            )
