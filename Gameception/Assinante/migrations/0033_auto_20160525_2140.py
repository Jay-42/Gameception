# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 00:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assinante', '0032_auto_20160525_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadosassinatura',
            name='tipoMidia',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Assinante.TipoMidia'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dadosassinatura',
            name='sistOp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assinante.SistOp'),
        ),
    ]
