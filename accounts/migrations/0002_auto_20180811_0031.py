# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-10 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, choices=[('Student', 'Student'), ('Teacher', 'Teacher')], max_length=10, null=True),
        ),
    ]
