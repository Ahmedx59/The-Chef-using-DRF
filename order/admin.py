from django.contrib import admin

from order.models import Cart , CartItem , Order , OrderItem


class CartItemTabularInline(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = (CartItemTabularInline,)
    list_display = ("user",)


class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemTabularInline,)
    list_display = ("user",)


admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)