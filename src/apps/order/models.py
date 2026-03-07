from django.db import models
from apps.product.models import Product
from apps.customer.models import Customer
from apps.users.models import Stuff

# Create your models here.

class Cart(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    stuff=models.ForeignKey(Stuff, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product}"
    
class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    stuff=models.ForeignKey(Stuff, on_delete=models.CASCADE)
    total_price=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    PAYMENT_CHOICES=[
        ("cash", "Cash"),
        ("cart", "Cart"),
    ]
    payment_type=models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer}, {self.stuff}, {self.total_price}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    stuff=models.ForeignKey(Stuff, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    total_price=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order}, {self.product}, {self.stuff}"



