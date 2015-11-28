# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0003_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='comment',
            field=models.CharField(verbose_name='Invitation Comment', blank=True, max_length=300, help_text='Write some comment to the user when invitating'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='to_user',
            field=models.ForeignKey(verbose_name='User to Invite', related_name='to_invitations', to=settings.AUTH_USER_MODEL),
        ),
    ]
