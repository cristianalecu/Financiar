# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financiar', '0003_auto_20171009_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='title',
            field=models.CharField(max_length=100, default=' '),
        ),
    ]
