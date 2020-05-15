from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
#     username = models.CharField(max_length=125,blank=False)
#     password = models.CharField(max_length=20,blank=False)
#     firstname = models.CharField(blank=False,max_length=30,default=None)
#     lastname = models.CharField(blank=False,max_length=30,default=None)
#     email = models.EmailField(blank=False,default=None)
    contact_number = models.DecimalField(max_digits=10,decimal_places=0,blank=False,default=None)
    #birthdate = models.DateField(blank=False,default=None)
    image = models.ImageField(default='default.jpg',upload_to='prfile_pics')  
    
    def __str__(self):
        return f'{self.user.username} Profile'