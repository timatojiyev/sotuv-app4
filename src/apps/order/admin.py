from django.contrib import admin
from .models import Order, OrderItem, Cart

# Register your models here.

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(OrderItem)
