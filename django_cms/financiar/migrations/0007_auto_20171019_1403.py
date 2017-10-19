# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financiar', '0006_auto_20171018_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationFinal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.PositiveIntegerField(default=1)),
                ('title', models.CharField(max_length=100, default=' ')),
                ('year', models.PositiveSmallIntegerField(default=2017)),
                ('month', models.PositiveSmallIntegerField(default=1)),
                ('base', models.FloatField(default=0)),
                ('trend', models.FloatField(default=0)),
                ('infla', models.FloatField(default=0)),
                ('actions', models.FloatField(default=0)),
                ('matur', models.FloatField(default=0)),
                ('traffic', models.FloatField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='LocationFull',
        ),
        migrations.AlterField(
            model_name='channelbrandindicator',
            name='bbenchmark',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='channelbrandindicator',
            name='bbrand',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='channelbrandindicator',
            name='bchannel',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='location',
            name='bbenchmark',
            field=models.ForeignKey(null=True, related_name='locations_B', on_delete=django.db.models.deletion.SET_NULL, to='financiar.Benchmark'),
        ),
        migrations.AlterField(
            model_name='location',
            name='brand',
            field=models.ForeignKey(null=True, related_name='locations', on_delete=django.db.models.deletion.SET_NULL, to='financiar.Brand'),
        ),
        migrations.AlterField(
            model_name='location',
            name='category',
            field=models.ForeignKey(null=True, related_name='locations', on_delete=django.db.models.deletion.SET_NULL, to='financiar.Category'),
        ),
        migrations.AlterField(
            model_name='location',
            name='channel',
            field=models.ForeignKey(null=True, related_name='locations', on_delete=django.db.models.deletion.SET_NULL, to='financiar.Channel'),
        ),
        migrations.AlterField(
            model_name='location',
            name='cn_vs_B',
            field=models.ForeignKey(null=True, related_name='locations_vsB', on_delete=django.db.models.deletion.SET_NULL, to='financiar.ConstNetwork'),
        ),
        migrations.AlterField(
            model_name='location',
            name='cn_vs_H',
            field=models.ForeignKey(null=True, related_name='locations_vsH', on_delete=django.db.models.deletion.SET_NULL, to='financiar.ConstNetwork'),
        ),
        migrations.AlterField(
            model_name='location',
            name='ebenchmark',
            field=models.ForeignKey(null=True, related_name='locations_E', on_delete=django.db.models.deletion.SET_NULL, to='financiar.Benchmark'),
        ),
        migrations.AlterField(
            model_name='location',
            name='sales_concept',
            field=models.ForeignKey(null=True, related_name='locations', on_delete=django.db.models.deletion.SET_NULL, to='financiar.SalesConcept'),
        ),
        migrations.AlterField(
            model_name='location',
            name='sales_concept_size',
            field=models.ForeignKey(null=True, related_name='locations', on_delete=django.db.models.deletion.SET_NULL, to='financiar.SalesConceptSize'),
        ),
        migrations.AlterField(
            model_name='location',
            name='subcategory',
            field=models.ForeignKey(null=True, related_name='locations', on_delete=django.db.models.deletion.SET_NULL, to='financiar.Subcategory'),
        ),
    ]
