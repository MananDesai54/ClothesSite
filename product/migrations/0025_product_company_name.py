# Generated by Django 3.0.1 on 2020-03-19 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_wishlist_imagepath'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='company_name',
            field=models.CharField(default=None, max_length=150, null=True),
        ),
    ]
