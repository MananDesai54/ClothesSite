# Generated by Django 3.0.1 on 2020-03-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
