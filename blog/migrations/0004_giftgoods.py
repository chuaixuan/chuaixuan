# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170519_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftGoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('classname', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=201)),
                ('price', models.FloatField(max_length=200)),
                ('unit', models.CharField(max_length=200)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
