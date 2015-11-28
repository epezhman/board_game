# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tictactoe', '0002_game_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('sent_time', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(related_name='from_invitations', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='to_invitations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
