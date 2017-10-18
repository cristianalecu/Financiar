# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financiar', '0005_auto_20171018_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channelbrandindicator',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='channelbrandindicator',
            name='category',
        ),
        migrations.RemoveField(
            model_name='channelbrandindicator',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='channelbrandindicator',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='channelbrandindicator',
            name='bbenchmark',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='channelbrandindicator',
            name='bbrand',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='channelbrandindicator',
            name='bcategory',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='channelbrandindicator',
            name='bchannel',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='channelbrandindicator',
            name='bsalesconcept',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='channelbrandindicator',
            name='bsalesconceptsize',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='channelbrandindicator',
            name='bsubcategory',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='channelbrandindicator',
            name='ebenchmarks',
            field=models.ManyToManyField(blank=True, to='financiar.Benchmark'),
        ),
        migrations.AddField(
            model_name='channelbrandindicator',
            name='salesconcepts',
            field=models.ManyToManyField(blank=True, to='financiar.SalesConcept'),
        ),
        migrations.AddField(
            model_name='channelbrandindicator',
            name='salesconceptsizes',
            field=models.ManyToManyField(blank=True, to='financiar.SalesConceptSize'),
        ),
        migrations.AlterField(
            model_name='channelbrandindicator',
            name='brands',
            field=models.ManyToManyField(blank=True, to='financiar.Brand'),
        ),
        migrations.AlterField(
            model_name='channelbrandindicator',
            name='categories',
            field=models.ManyToManyField(blank=True, to='financiar.Category'),
        ),
        migrations.AlterField(
            model_name='channelbrandindicator',
            name='channels',
            field=models.ManyToManyField(blank=True, to='financiar.Channel'),
        ),
        migrations.AlterField(
            model_name='channelbrandindicator',
            name='subcategories',
            field=models.ManyToManyField(blank=True, to='financiar.Subcategory'),
        ),
    ]
