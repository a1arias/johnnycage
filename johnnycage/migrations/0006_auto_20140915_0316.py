# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('johnnycage', '0005_auto_20140915_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='mainstatement',
            field=models.TextField(max_length=400, default='Change me to something crafty or witty'),
        ),
    ]
