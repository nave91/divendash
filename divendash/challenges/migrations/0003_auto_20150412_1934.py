# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='challenges',
        ),
        migrations.AddField(
            model_name='challenge',
            name='game',
            field=models.ManyToManyField(to='challenges.Game'),
        ),
    ]
