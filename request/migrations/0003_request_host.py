# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='host',
            field=models.CharField(verbose_name='path', default='', max_length=255),
            preserve_default=False,
        ),
    ]
