# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_auto_20170314_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='clase',
            name='lectura',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='clase',
            name='tema',
            field=models.CharField(max_length=100),
        ),
    ]