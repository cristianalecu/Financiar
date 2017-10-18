# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financiar', '0003_salesdata_matur'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraficData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('year', models.PositiveSmallIntegerField(default=2017)),
                ('month', models.PositiveSmallIntegerField(default=1)),
                ('trend', models.FloatField(default=0)),
                ('inflation', models.FloatField(default=0)),
                ('commercial_actions', models.FloatField(default=0)),
                ('matur', models.FloatField(default=0)),
                ('traffic', models.FloatField(default=0)),
                ('fullx', models.FloatField(default=0)),
            ],
        ),
    ]
