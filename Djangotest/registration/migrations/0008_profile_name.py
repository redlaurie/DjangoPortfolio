# Generated by Django 3.1.3 on 2021-01-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=24, null=True),
        ),
    ]
