# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-22 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20180218_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificationCode', models.IntegerField(max_length=10)),
                ('initials', models.CharField(max_length=10)),
            ],
        ),
    ]