from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.utils.crypto import get_random_string




class User(AbstractUser):
    class UserType(models.TextChoices):
        SELLER = 'Seller'
        USER = 'User'

    email = models.EmailField(max_length=500 , unique=True)
    username = models.CharField(max_length=100 )
    image = models.ImageField(upload_to='user_image' , blank=True)
    user_type = models.CharField(max_length=50 , choices=UserType.choices , default=UserType.USER)
    code = models.CharField(max_length=50 , blank=True)
    code_expire_date = models.DateTimeField(blank=True, null=True)

    # username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_type","username"]

    def __str__(self)-> str:
        return self.email
    

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = get_random_string(20)
       
        super().save(*args, **kwargs)