from django.contrib import admin

from order.models import Cart , MealsDetail , Order

admin.site.register(Cart)
admin.site.register(MealsDetail)
admin.site.register(Order)