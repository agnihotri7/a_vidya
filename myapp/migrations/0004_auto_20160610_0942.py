# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20160610_0727'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profiles',
            options={'permissions': (('view_profile', 'Can view profiles'), ('download_profiles', 'Can download profiles'))},
        ),
    ]
