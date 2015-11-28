# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0004_auto_20151127_1525'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='move',
            options={'get_latest_by': 'timestamp'},
        ),
        migrations.AddField(
            model_name='move',
            name='by_first_plyer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='move',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 28, 11, 35, 46, 242177), auto_now_add=True),
            preserve_default=False,
        ),
    ]
