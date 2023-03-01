<<<<<<< HEAD
# Generated by Django 4.1.7 on 2023-02-28 21:35
=======
# Generated by Django 4.1.7 on 2023-02-21 22:15
>>>>>>> master

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('operacao', models.CharField(choices=[('SI', 'Simples'), ('RA', 'Rateio')], max_length=2)),
                ('situacao', models.CharField(default='A', max_length=1)),
            ],
            options={
                'verbose_name': 'Conta',
                'verbose_name_plural': 'Contas',
            },
        ),
    ]
