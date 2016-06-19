# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assinante', '0054_auto_20160608_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='descricao',
            field=models.CharField(default='x y z', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jogo',
            name='memRAM',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dadosassinatura',
            name='sistOp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Assinante.SistOp'),
        ),
    ]
