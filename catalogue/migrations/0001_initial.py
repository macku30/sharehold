# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-13 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardGameItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemLabel', models.CharField(max_length=30)),
                ('codeType', models.CharField(choices=[('BAR', 'Barcode'), ('QR', 'QR code')], default='BAR', max_length=3)),
                ('codeValue', models.CharField(max_length=20, null=True)),
                ('bggURL', models.URLField(max_length=100)),
                ('basegame', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extensions', to='catalogue.BoardGameItem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
