# Generated by Django 4.1.7 on 2023-02-21 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condominio',
            name='Bairro',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='condominio',
            name='CEP',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='condominio',
            name='Cidade',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='condominio',
            name='Endereco',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='condominio',
            name='Estado',
            field=models.CharField(max_length=2),
        ),
        migrations.CreateModel(
            name='bloco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('situacao', models.CharField(default='A', max_length=1)),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.condominio')),
            ],
        ),
    ]
