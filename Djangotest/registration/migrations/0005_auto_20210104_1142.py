# Generated by Django 3.1.3 on 2021-01-04 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_order_orderitem_product_shippingaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='Profile',
        ),
    ]
