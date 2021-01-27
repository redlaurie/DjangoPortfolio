# Generated by Django 3.1.3 on 2021-01-27 11:17

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_profile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, null=True)),
                ('description', models.TextField(default='Hello', verbose_name=django.contrib.auth.models.User)),
                ('Profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.profile')),
            ],
        ),
    ]
