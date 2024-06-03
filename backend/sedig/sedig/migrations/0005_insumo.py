# Generated by Django 5.0.6 on 2024-06-03 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sedig', '0004_orcamento_patio_modulomanobra_moduloequipamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_insumo', models.CharField(max_length=255)),
                ('nome', models.CharField(max_length=255)),
                ('local', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField()),
                ('preco_unitario', models.FloatField()),
                ('custo', models.FloatField()),
            ],
        ),
    ]
