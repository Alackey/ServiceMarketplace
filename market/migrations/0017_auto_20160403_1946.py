# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0016_auto_20160403_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='final_time',
            field=models.DateTimeField(),
        ),
    ]
