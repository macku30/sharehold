# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-25 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circulation', '0002_auto_20180225_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentalclient',
            old_name='initials',
            new_name='name',
        ),
    ]
