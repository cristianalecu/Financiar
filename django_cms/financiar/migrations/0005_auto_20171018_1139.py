# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financiar', '0004_graficdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='channelbrandindicator',
            name='brands',
            field=models.ManyToManyField(to='financiar.Brand'),
        ),
        migrations.AddField(
            model_name='channelbrandindicator',
            name='categories',
            field=models.ManyToManyField(to='financiar.Category'),
        ),
        migrations.AddField(
            model_name='channelbrandindicator',
            name='channels',
            field=models.ManyToManyField(to='financiar.Channel'),
        ),
        migrations.AddField(
            model_name='channelbrandindicator',
            name='subcategories',
            field=models.ManyToManyField(to='financiar.Subcategory'),
        ),
        migrations.AddField(
            model_name='graficdata',
            name='base',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='location',
            name='opened_from',
            field=models.DateField(default='2016-01-01'),
        ),
        migrations.AddField(
            model_name='location',
            name='opened_to',
            field=models.DateField(default='2019-12-01'),
        ),
        migrations.AddField(
            model_name='locationfull',
            name='opened_from',
            field=models.DateField(default='2016-01-01'),
        ),
        migrations.AddField(
            model_name='locationfull',
            name='opened_to',
            field=models.DateField(default='2019-12-01'),
        ),
    ]
