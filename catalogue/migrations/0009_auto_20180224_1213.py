# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-24 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_auto_20180224_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgameitem',
            name='baseGameItem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extensions', related_query_name='basegame', to='catalogue.BoardGameItem'),
        ),
    ]
