# Generated by Django 4.1.7 on 2023-02-21 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0005_contas_operacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contas',
            name='operacao',
            field=models.CharField(choices=[('SI', 'Simples'), ('RA', 'Rateio')], max_length=2),
        ),
    ]
