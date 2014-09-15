# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('johnnycage', '0002_auto_20140915_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='mainreadmorebtn',
            field=models.CharField(default='Read more&raquo;', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='readmorebtn',
            field=models.CharField(default='Continue Reading&raquo;', max_length=50),
            preserve_default=True,
        ),
    ]
