# Generated by Django 3.1.3 on 2021-01-28 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_diaryitem_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaryitem',
            name='Profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.profile'),
        ),
    ]