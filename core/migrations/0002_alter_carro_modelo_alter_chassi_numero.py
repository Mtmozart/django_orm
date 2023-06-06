# Generated by Django 4.2.2 on 2023-06-06 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='modelo',
            field=models.CharField(help_text='Máximo 30 caracteres', max_length=30, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='chassi',
            name='numero',
            field=models.CharField(help_text='Máximo 16 caracteres', max_length=16, verbose_name='Chassi'),
        ),
    ]
