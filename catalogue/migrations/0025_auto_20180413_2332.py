# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-13 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0024_auto_20180413_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgameitem',
            name='itemImage',
            field=models.ImageField(blank=True, null=True, upload_to='catalogue/bg/'),
        ),
    ]
