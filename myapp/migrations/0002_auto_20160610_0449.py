# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('cdt', models.DateTimeField(auto_now_add=True)),
                ('mdt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'designations',
            },
        ),
        migrations.AlterField(
            model_name='profiles',
            name='current_designation',
            field=models.ForeignKey(to='myapp.Designation'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='experience',
            field=models.IntegerField(default=1, choices=[(1, b'0.0-1.0'), (2, b'1.0-2.0'), (3, b'2.0-3.0'), (4, b'3.0-4.0'), (5, b'4.0-5.0'), (6, b'5.0-6.0'), (7, b'6.0-7.0'), (8, b'7.0-8.0'), (9, b'8.0-9.0'), (10, b'9.0-10.0'), (11, b'10.0-15.0')]),
        ),
    ]
