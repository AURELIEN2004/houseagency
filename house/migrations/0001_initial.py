# Generated by Django 5.1.6 on 2025-03-11 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('appartement', 'Appartement'), ('maison', 'Maison'), ('studio', 'Studio'), ('chambre', 'Chambre')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('region', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('area', models.PositiveIntegerField()),
                ('image', models.URLField(blank=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
