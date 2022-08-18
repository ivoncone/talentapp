# Generated by Django 4.0.3 on 2022-07-02 21:22

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('empresa', models.CharField(max_length=250)),
                ('descrip', models.CharField(max_length=300, null=True)),
                ('web', models.URLField(max_length=250, unique=True)),
                ('rfc', models.CharField(max_length=20, unique=True)),
                ('logo', cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/posdatamexicogallery/image/upload/v1656036804/avatares/default_riyo2u.jpg', max_length=255, null=True, verbose_name='image')),
                ('is_approved', models.BooleanField(default=False)),
                ('is_declined', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'empresas',
                'ordering': ['-updated_at'],
            },
        ),
    ]
