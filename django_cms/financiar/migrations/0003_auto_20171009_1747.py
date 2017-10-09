# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financiar', '0002_salesdata_open'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrendData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('year', models.PositiveSmallIntegerField(default=2017)),
                ('month', models.PositiveSmallIntegerField(default=1)),
                ('trend', models.FloatField(default=0)),
                ('inflation', models.FloatField(default=0)),
                ('commercial_actions', models.FloatField(default=0)),
                ('brand', models.ForeignKey(related_name='trend_data', to='financiar.Brand')),
                ('category', models.ForeignKey(related_name='trend_data', to='financiar.Category')),
                ('channel', models.ForeignKey(related_name='trend_data', to='financiar.Channel')),
                ('subcategory', models.ForeignKey(related_name='trend_data', to='financiar.Subcategory')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='number',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='location',
            name='title',
            field=models.CharField(max_length=100, default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salesdata',
            name='maturity',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='salesdata',
            name='traffic',
            field=models.FloatField(default=0),
        ),
        migrations.AlterIndexTogether(
            name='salesdata',
            index_together=set([('location', 'year', 'month')]),
        ),
    ]
