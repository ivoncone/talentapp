# Generated by Django 4.0.3 on 2022-07-11 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacante',
            name='jobrole',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]