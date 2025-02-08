# Generated by Django 5.1.6 on 2025-02-08 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('data_nascimento', models.DateField()),
                ('serie', models.CharField(max_length=20)),
                ('matricula', models.CharField(max_length=20, unique=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
