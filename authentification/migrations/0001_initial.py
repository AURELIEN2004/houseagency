# Generated by Django 5.1.7 on 2025-03-25 11:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('house', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Locataire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('profile_image', models.ImageField(blank=True, upload_to='authentification/')),
                ('logements', models.ManyToManyField(related_name='locataire', to='house.logement')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='locataire', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Proprietaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('profile_image', models.ImageField(blank=True, upload_to='authentification/')),
                ('logements', models.ManyToManyField(related_name='proprietaire', to='house.logement')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='proprietaire', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
