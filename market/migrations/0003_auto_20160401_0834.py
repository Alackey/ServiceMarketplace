# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_service_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]