# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-22 15:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlehit',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 22, 15, 14, 41, 218263, tzinfo=utc)),
        ),
    ]
