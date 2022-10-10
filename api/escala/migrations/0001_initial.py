# Generated by Django 4.1 on 2022-10-09 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(choices=[('g1', 'Grupo_1'), ('g2', 'Grupo_2'), ('g3', 'Grupo_3'), ('g4', 'Grupo_4')], default='g1', max_length=2, verbose_name='Group')),
                ('date', models.DateField(verbose_name='Date')),
                ('road', models.CharField(max_length=20, verbose_name='Road')),
                ('begin', models.TimeField(verbose_name='Begin')),
                ('end', models.TimeField(verbose_name='End')),
                ('foothold', models.CharField(max_length=250, verbose_name='FootHold')),
                ('worker', models.CharField(max_length=120, verbose_name='Worker')),
                ('zone', models.CharField(max_length=20, verbose_name='Zone')),
            ],
        ),
    ]
