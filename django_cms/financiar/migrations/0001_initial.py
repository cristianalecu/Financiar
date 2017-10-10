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
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='benchmark', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='brands', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CBIndicatorData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('year', models.PositiveSmallIntegerField(default=2017)),
                ('month', models.PositiveSmallIntegerField(default=1)),
                ('trend', models.FloatField(default=0)),
                ('inflation', models.FloatField(default=0)),
                ('commercial_actions', models.FloatField(default=0)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='channels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChannelBrandIndicator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(related_name='indicators', to='financiar.Brand')),
                ('category', models.ForeignKey(related_name='indicators', to='financiar.Category')),
                ('channel', models.ForeignKey(related_name='indicators', to='financiar.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='ConstNetwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='const_networks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=5)),
                ('number', models.PositiveSmallIntegerField(default=1)),
                ('title', models.CharField(max_length=100, default=' ')),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('bbenchmark', models.ForeignKey(related_name='locations_B', to='financiar.Benchmark')),
                ('brand', models.ForeignKey(related_name='locations', to='financiar.Brand')),
                ('category', models.ForeignKey(related_name='locations', to='financiar.Category')),
                ('channel', models.ForeignKey(related_name='locations', to='financiar.Channel')),
                ('cn_vs_B', models.ForeignKey(related_name='locations_vsB', to='financiar.ConstNetwork')),
                ('cn_vs_H', models.ForeignKey(related_name='locations_vsH', to='financiar.ConstNetwork')),
                ('ebenchmark', models.ForeignKey(related_name='locations_E', to='financiar.Benchmark')),
            ],
        ),
        migrations.CreateModel(
            name='SalesConcept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='sales_concepts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalesConceptSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='sales_conceptsize', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalesData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('year', models.PositiveSmallIntegerField(default=2017)),
                ('month', models.PositiveSmallIntegerField(default=1)),
                ('open', models.BooleanField(default=True)),
                ('value', models.FloatField(default=0)),
                ('traffic', models.FloatField(default=0)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('type', models.PositiveIntegerField(default=0, choices=[(0, 'Sales value'), (10, 'Simulate'), (20, 'ProjectedLvl1'), (21, 'ProjectedLvl2'), (22, 'ProjectedLvl3'), (30, 'ToBeDeleted'), (40, 'Other')])),
                ('location', models.ForeignKey(related_name='sales_data', to='financiar.Location')),
                ('user', models.ForeignKey(related_name='sales_data', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='subcategories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='sales_concept',
            field=models.ForeignKey(related_name='locations', to='financiar.SalesConcept'),
        ),
        migrations.AddField(
            model_name='location',
            name='sales_concept_size',
            field=models.ForeignKey(related_name='locations', to='financiar.SalesConceptSize'),
        ),
        migrations.AddField(
            model_name='location',
            name='subcategory',
            field=models.ForeignKey(related_name='locations', to='financiar.Subcategory'),
        ),
        migrations.AddField(
            model_name='location',
            name='user',
            field=models.ForeignKey(related_name='locations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='channelbrandindicator',
            name='subcategory',
            field=models.ForeignKey(related_name='indicators', to='financiar.Subcategory'),
        ),
        migrations.AddField(
            model_name='channelbrandindicator',
            name='user',
            field=models.ForeignKey(related_name='cbindicators', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cbindicatordata',
            name='indicator',
            field=models.ForeignKey(related_name='indicator_data', to='financiar.ChannelBrandIndicator'),
        ),
        migrations.AddField(
            model_name='cbindicatordata',
            name='user',
            field=models.ForeignKey(related_name='cbindicatordata', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterIndexTogether(
            name='salesdata',
            index_together=set([('location', 'year', 'month')]),
        ),
    ]
