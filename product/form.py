from django import forms
from .models import Product

class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'sub_catagory',
            'stock',
            'price',
            'img1',
            'img2',
            'img3',
            'img4',
            'img5',
        ]
