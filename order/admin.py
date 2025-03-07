from django.contrib import admin

from order.models import Cart , CartItem , Order


class CartItemTabularInline(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = (CartItemTabularInline,)
    list_display = ("user","is_completed","coupon",)




admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem)
admin.site.register(Order)