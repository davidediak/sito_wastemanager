# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-22 18:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20180822_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlehit',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 22, 18, 23, 17, 129177, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sessionbind',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 22, 18, 23, 17, 129177, tzinfo=utc)),
        ),
    ]
