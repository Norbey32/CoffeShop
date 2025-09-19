from django.contrib import admin

from .models import Order, OrderProduct


class OrderProductInLine(admin.TabularInline):
    model = OrderProduct
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderProductInLine
        ]

admin.site.register(Order, OrderAdmin)
