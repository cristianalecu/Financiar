# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financiar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CBIndicatorFull',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('channel', models.CharField(max_length=100, default=' ')),
                ('brand', models.CharField(max_length=100, default=' ')),
                ('category', models.CharField(max_length=100, default=' ')),
                ('subcategory', models.CharField(max_length=100, default=' ')),
            ],
        ),
        migrations.CreateModel(
            name='LocationFull',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=5)),
                ('number', models.PositiveSmallIntegerField(default=1)),
                ('title', models.CharField(max_length=100, default=' ')),
                ('channel', models.CharField(max_length=100, default=' ')),
                ('brand', models.CharField(max_length=100, default=' ')),
                ('category', models.CharField(max_length=100, default=' ')),
                ('subcategory', models.CharField(max_length=100, default=' ')),
                ('ebenchmark', models.CharField(max_length=100, default=' ')),
                ('bbenchmark', models.CharField(max_length=100, default=' ')),
                ('sales_concept', models.CharField(max_length=100, default=' ')),
                ('sales_concept_size', models.CharField(max_length=100, default=' ')),
                ('cn_vs_H', models.CharField(max_length=100, default=' ')),
                ('cn_vs_B', models.CharField(max_length=100, default=' ')),
            ],
        ),
        migrations.CreateModel(
            name='Lookup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
