from django.contrib import admin
from .models import Product,Cart,CartProducts,WishList
# # Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartProducts)
admin.site.register(WishList)