# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Benchmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ConstNetwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SalesConcept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SalesConceptSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SalesData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('year', models.PositiveSmallIntegerField(default=2017)),
                ('month', models.PositiveSmallIntegerField(default=1)),
                ('project', models.BooleanField(default=True)),
                ('value', models.FloatField(default=0)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('type', models.PositiveIntegerField(default=0, choices=[(0, 'Sales value'), (10, 'Simulate'), (20, 'ProjectedLvl1'), (21, 'ProjectedLvl2'), (22, 'ProjectedLvl3'), (30, 'ToBeDeleted'), (40, 'Other')])),
                ('bbenchmark', models.ForeignKey(related_name='sales_data_B', to='financiar.Benchmark')),
                ('brand', models.ForeignKey(related_name='sales_data', to='financiar.Brand')),
                ('category', models.ForeignKey(related_name='sales_data', to='financiar.Category')),
                ('channel', models.ForeignKey(related_name='sales_data', to='financiar.Channel')),
                ('cn_vs_B', models.ForeignKey(related_name='sales_data_vsB', to='financiar.ConstNetwork')),
                ('cn_vs_H', models.ForeignKey(related_name='sales_data_vsH', to='financiar.ConstNetwork')),
                ('ebenchmark', models.ForeignKey(related_name='sales_data_E', to='financiar.Benchmark')),
                ('location', models.ForeignKey(related_name='sales_data', to='financiar.Location')),
                ('sales_concept', models.ForeignKey(related_name='sales_data', to='financiar.SalesConcept')),
                ('sales_concept_size', models.ForeignKey(related_name='sales_data', to='financiar.SalesConceptSize')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='salesdata',
            name='subcategory',
            field=models.ForeignKey(related_name='sales_data', to='financiar.Subcategory'),
        ),
        migrations.AddField(
            model_name='salesdata',
            name='user',
            field=models.ForeignKey(related_name='sales_data', to=settings.AUTH_USER_MODEL),
        ),
    ]
