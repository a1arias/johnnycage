# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('johnnycage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='mainstatement',
            field=models.CharField(default='Change me to something crafty or witty', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='subtitle',
            field=models.CharField(default='What else?', max_length=200),
            preserve_default=True,
        ),
    ]
