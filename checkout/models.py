from django.db import models

# Create your models here.

class OrderDetails(models.Model):
    username = models.CharField(null=False,max_length=150)
    product_name = models.CharField(null=False,max_length=150)
    address = models.CharField(null=False,max_length=500)
    sub_address = models.CharField(default=None,max_length=200)
    country = models.CharField(null=False,max_length=100)
    state = models.CharField(null=False,max_length=100)
    city = models.CharField(null=False,max_length=100)
    pincode = models.IntegerField(null=False)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    imagepath = models.CharField(default=None,max_length=1000)