# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=200, default='Change Me')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
