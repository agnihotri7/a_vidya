# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('cdt', models.DateTimeField(auto_now_add=True)),
                ('mdt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sno', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('resume', models.IntegerField(default=2, choices=[(1, b'Yes'), (2, b'No')])),
                ('experience', models.DecimalField(max_digits=20, decimal_places=2)),
                ('ctc', models.DecimalField(max_digits=20, decimal_places=2)),
                ('current_employer', models.CharField(max_length=30)),
                ('current_designation', models.CharField(max_length=30)),
                ('cdt', models.DateTimeField(auto_now_add=True)),
                ('mdt', models.DateTimeField(auto_now=True)),
                ('current_city', models.ForeignKey(to='myapp.City')),
                ('preferred_city', models.ForeignKey(related_name='profile', to='myapp.City')),
            ],
            options={
                'db_table': 'profiles',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('cdt', models.DateTimeField(auto_now_add=True)),
                ('mdt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'skills',
            },
        ),
        migrations.AddField(
            model_name='profiles',
            name='skills',
            field=models.ManyToManyField(to='myapp.Skill'),
        ),
    ]
