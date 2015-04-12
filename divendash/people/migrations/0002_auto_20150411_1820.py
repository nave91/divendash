# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Customer',
            new_name='Member',
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ForeignKey(to='people.Member'),
        ),
    ]
