# Generated by Django 4.0.6 on 2022-08-09 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacantes', '0003_alter_vacante_descripcion_alter_vacante_requisitos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacante',
            name='descripcion',
            field=models.TextField(max_length=2500),
        ),
        migrations.AlterField(
            model_name='vacante',
            name='pregunta_1',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='vacante',
            name='pregunta_2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='vacante',
            name='pregunta_3',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='vacante',
            name='requisitos',
            field=models.TextField(max_length=2500),
        ),
    ]