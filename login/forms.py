from django import forms
from .models import Profile
from django.contrib.auth.models import User
from product.models import Product

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            # 'contact_number',
            # 'birthdate',
            'image',
        ]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_id',
            'product_number',
            'product_name',
            'company_name',
            'catagory',
            'sub_catagory',
            'stock',
            'price',
            'img1',
            'img2',
            'img3',
            'img4',
            'img5'
        ]

class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'catagory',
            'sub_catagory',
            'company_name',
            'stock',
            'price',
            'img1',
            'img2',
            'img3',
            'img4',
            'img5',
        ]
