# Generated by Django 4.1 on 2022-10-09 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escala', '0003_alter_escala_equipment_alter_escala_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escala',
            name='equipment',
            field=models.CharField(blank=True, choices=[('vtr', 'Viatura'), ('mt', 'Moto')], max_length=3, verbose_name='Equipment'),
        ),
    ]