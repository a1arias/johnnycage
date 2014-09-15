# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('johnnycage', '0003_auto_20140915_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slogan',
            field=models.CharField(default='Another cool site by adri.codes', max_length=150),
            preserve_default=True,
        ),
    ]
