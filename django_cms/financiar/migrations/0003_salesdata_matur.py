# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financiar', '0002_cbindicatorfull_locationfull_lookup'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesdata',
            name='matur',
            field=models.FloatField(default=0),
        ),
    ]
