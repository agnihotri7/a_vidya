# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20160610_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='experience',
            field=models.DecimalField(max_digits=20, decimal_places=2),
        ),
    ]
