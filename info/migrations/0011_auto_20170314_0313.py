# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_auto_20170302_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='lectura',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='clase',
            name='linkCap',
            field=models.FileField(blank=True, upload_to='libros/'),
        ),
        migrations.AlterField(
            model_name='clase',
            name='linkLectura',
            field=models.URLField(blank=True),
        ),
    ]
