# Generated by Django 3.1.3 on 2021-01-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_postimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimages',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
