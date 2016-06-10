# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20160610_0942'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profiles',
            options={'permissions': (('can_view_profile', 'Can view profiles'), ('can_download_profiles', 'Can download profiles'))},
        ),
    ]
