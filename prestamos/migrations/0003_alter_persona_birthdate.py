# Generated by Django 5.0.2 on 2024-03-01 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0002_remove_persona_firstname_remove_persona_secondname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='birthdate',
            field=models.DateField(default=None, null=True),
        ),
    ]
