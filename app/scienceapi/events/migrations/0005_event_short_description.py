# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_remove_event_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='short_description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]