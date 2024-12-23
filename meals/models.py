from django.db import models
from restaurant.models import Restaurant

class Meals(models.Model):
    class TabType(models.TextChoices):
        NEW = 'New'

    restaurant = models.ForeignKey(Restaurant, verbose_name='meals_restaurant', on_delete=models.CASCADE) 
    chief = models.ForeignKey('Chief' , on_delete=models.CASCADE , related_name = 'meals_chief' , blank=True, null=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='meals_image/' , blank=True, null=True)
    size = models.CharField(max_length=50 , blank=True, null=True)
    quantity = models.IntegerField()
    preparation_time = models.DateTimeField()
    desc = models.TextField()
    offer = models.CharField(max_length=50 , blank=True, null=True)
    tag = models.CharField(max_length=50 , choices= TabType.choices , default = TabType.NEW )


    def __str__(self)-> str:
        return self.name

class Chief (models.Model):
    class GenderType(models.TextChoices):
        MALE = 'Male'
        FEMALE = 'Female'


    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='chief/')
    gender = models.CharField(max_length=50 , choices= GenderType.choices )
    years_of_experience = models.IntegerField()


    def __str__(self)-> str:
        return self.name