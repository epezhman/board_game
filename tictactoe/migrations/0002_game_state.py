# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='state',
            field=models.CharField(choices=[('A', 'Active Game'), ('F', 'First Player Won'), ('S', 'Second Player Won'), ('L', 'Lost Game')], default='A', max_length=1),
        ),
    ]
