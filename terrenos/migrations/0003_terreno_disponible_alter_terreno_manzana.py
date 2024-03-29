# Generated by Django 4.1.7 on 2023-02-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrenos', '0002_remove_terreno_propietario_terreno_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='terreno',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='terreno',
            name='manzana',
            field=models.CharField(choices=[('A', 'Mz A, no existe'), ('B', 'Mz B'), ('G', 'Mz G'), ('H', 'Mz H'), ("H'", 'Mz H prima'), ('I', 'Mz I'), ('J', 'Mz J'), ('K', 'Mz K'), ('M', 'Mz M'), ('Ñ', 'Mz Ñ'), ('O', 'Mz O'), ('P', 'Mz P'), ('Q', 'Mz Q'), ('R', 'Mz R'), ('S', 'Mz S'), ('T', 'Mz T'), ('U', 'Mz U'), ('V', 'Mz V'), ('X', 'Mz X')], max_length=2),
        ),
    ]
