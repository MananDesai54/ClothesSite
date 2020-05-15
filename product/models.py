from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.IntegerField(primary_key=True,auto_created=True)
    product_number = models.CharField(default=None,max_length=20)
    company_name = models.CharField(default=None,max_length=150,null=True)
    product_name=models.CharField(default=None,null=False,max_length=100)
    catagory=models.CharField(default=None,max_length=50)
    sub_catagory=models.CharField(default=None,null=False,max_length=50)
    stock=models.IntegerField(default=0)
    price=models.FloatField(default=0.0,null=False)
    img1=models.ImageField(default='product.jpg',upload_to='product_pics')
    img2=models.ImageField(default='product.jpg',upload_to='product_pics')
    img3=models.ImageField(default='product.jpg',upload_to='product_pics')
    img4=models.ImageField(default='product.jpg',upload_to='product_pics')
    img5=models.ImageField(default='product.jpg',upload_to='product_pics')
    
    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)

class CartProducts(models.Model):
    # dict1 = {}
    # def __init__(self,user,product):
    #     if user==None or product==None:
    #         pass
    #     else:
    #         if not user in dict1:
    #             self.dict1[user] = []
    #         self.dict1[user].append(product)
    username = models.CharField(default=None,max_length=100,null=False)
    product_name = models.CharField(default=None,max_length=100,null=False)
    price=models.FloatField(default=0.0,null=False)
    quantity = models.IntegerField(default=1)
    imagePath = models.CharField(default=None,null=False,max_length=300)

class WishList(models.Model):
    username = models.CharField(default=None,max_length=150)
    product_name = models.CharField(default=None,max_length=150)
    price = models.FloatField(default=0.0,null=False)
    imagePath = models.CharField(default=None,null=False,max_length=300)
