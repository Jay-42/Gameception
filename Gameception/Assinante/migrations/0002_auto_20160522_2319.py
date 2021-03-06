# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assinante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosAssinatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('atividade', models.BooleanField(default=False)),
                ('memRAM', models.IntegerField()),
                ('memVideo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DadosBancarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroCartao', models.CharField(max_length=20)),
                ('codigoSeguranca', models.IntegerField()),
                ('nomeTitular', models.CharField(max_length=200)),
                ('vencimento', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EnderecoAssinatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=200)),
                ('numeroRua', models.IntegerField()),
                ('complemento', models.CharField(max_length=200)),
                ('CEP', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='assinante',
            name='CEP',
        ),
        migrations.RemoveField(
            model_name='assinante',
            name='complemento',
        ),
        migrations.RemoveField(
            model_name='assinante',
            name='numeroRua',
        ),
        migrations.RemoveField(
            model_name='assinante',
            name='rua',
        ),
        migrations.AlterField(
            model_name='assinante',
            name='CPF',
            field=models.CharField(max_length=14),
        ),
    ]
