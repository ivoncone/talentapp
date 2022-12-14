# Generated by Django 4.0.3 on 2022-07-06 00:01

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('intereses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CivilStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civil_status', models.CharField(max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'civilstatus',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=100, null=True, unique=True)),
            ],
            options={
                'db_table': 'genders',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('last_name_m', models.CharField(blank=True, max_length=120, null=True)),
                ('birth_date', models.DateField()),
                ('age', models.IntegerField()),
                ('contact_email', models.EmailField(blank=True, max_length=120, null=True)),
                ('residence', models.CharField(max_length=120)),
                ('image', cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/posdatamexicogallery/image/upload/v1656036804/avatares/default_riyo2u.jpg', max_length=255, verbose_name='image')),
                ('video', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='intereses.area')),
                ('civil_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.civilstatus')),
                ('genero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.gender')),
                ('jobrole', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='intereses.jobrole')),
                ('modalidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='intereses.modalidad')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='intereses.state')),
                ('tipo_trabajo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='intereses.tipotrabajo')),
            ],
            options={
                'db_table': 'personas',
            },
        ),
    ]
