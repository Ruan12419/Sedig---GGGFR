# Generated by Django 5.0.6 on 2024-06-01 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14)),
                ('chave_passe', models.CharField(blank=True, max_length=14, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('estado', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=255)),
            ],
        ),
    ]
