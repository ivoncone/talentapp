# Generated by Django 4.0.6 on 2022-07-28 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacantes', '0002_alter_vacante_jobrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacante',
            name='descripcion',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='vacante',
            name='requisitos',
            field=models.TextField(max_length=800),
        ),
    ]
