# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-22 18:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20180822_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlehit',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='articlehit',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 22, 18, 5, 36, 217127, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sessionbind',
            name='django_session_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessions.Session'),
        ),
        migrations.AlterField(
            model_name='sessionbind',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 22, 18, 5, 36, 217127, tzinfo=utc)),
        ),
    ]
