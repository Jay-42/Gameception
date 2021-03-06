# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 03:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assinante', '0002_auto_20160522_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='dadosassinatura',
            name='generosPessoais',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Assinante.Genero'),
            preserve_default=False,
        ),
    ]
