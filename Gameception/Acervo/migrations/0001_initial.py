# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.IntegerField()),
                ('disponivel', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=200)),
                ('img1', models.CharField(max_length=200)),
                ('img2', models.CharField(max_length=200)),
                ('tipoMidia', models.CharField(choices=[('FISICA', 'Fisica'), ('DIGITAL', 'Digital')], default='DIGITAL', max_length=10)),
                ('listaGeneros', models.ManyToManyField(to='Acervo.Genero')),
            ],
        ),
    ]