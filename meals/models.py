from django.db import models

class Meals(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='meals_image/')
    size = models.CharField(max_length=50)
    quantity = models.IntegerField()
    preparation_time = models.DateTimeField()
    desc = models.TextField()
    offer = models.CharField(max_length=50)
    tag = ''


class Chief (models.Model):
    meals = models.ForeignKey(Meals , on_delete=models.CASCADE , related_name = 'meals_chief')
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='chief/')
    gender = models.BooleanField()
    years_of_experience = models.IntegerField()