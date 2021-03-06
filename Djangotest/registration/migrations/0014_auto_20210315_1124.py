# Generated by Django 3.1.3 on 2021-03-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_profile_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dexterity',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='dexteritysteps',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='strength',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='strengthsteps',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
