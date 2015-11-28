# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0005_auto_20151128_1135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='move',
            old_name='by_first_plyer',
            new_name='by_first_player',
        ),
        migrations.AlterField(
            model_name='move',
            name='comment',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
