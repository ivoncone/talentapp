# Generated by Django 4.0.6 on 2022-07-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_application_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='video',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]