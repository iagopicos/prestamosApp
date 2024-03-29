# Generated by Django 5.0.2 on 2024-02-29 19:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('secondname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('persona_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.persona')),
                ('prestamo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.prestamo')),
            ],
        ),
        migrations.CreateModel(
            name='RawSolicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_data', models.CharField(max_length=500)),
                ('origin', models.CharField(max_length=20)),
                ('solicitud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.solicitud')),
            ],
        ),
    ]
