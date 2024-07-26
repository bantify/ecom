from datetime import datetime

from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    phone = models.CharField(max_length=50, null=False)
    # image = models.ImageField(upload_to='images/', null=False)
    createDate = models.DateTimeField(auto_now_add=True,null=True)
    updateDate = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    unit = {
        'kg': 'Kg',
        'lb': 'Lb',
        'liter': 'Liter',
        'g': 'G',
        'piece': 'Piece',
    }
    name = models.CharField(max_length=100, unique=True, null=False)
    price = models.FloatField(default=0,)
    discount = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    # image = models.ImageField(upload_to='images/', null=False)
    createDate = models.DateTimeField(auto_now_add=True,null=True)
    updateDate = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.name} - {self.price} - {self.discount}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.FloatField()
    createDate = models.DateTimeField(auto_now_add=True,null=True)
    updateDate = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.customer.name} - {self.total_price}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
