# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_purchased_goods_sumtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchased_goods',
            name='gift_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='purchased_goods',
            name='gift_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='purchased_goods',
            name='original_price',
            field=models.FloatField(default=0),
        ),
    ]
