# Generated by Django 5.1.7 on 2025-03-25 11:19

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
                ('categorie', models.CharField(choices=[('appartement', 'Appartement'), ('maison', 'Maison'), ('studio', 'Studio'), ('chambre', 'Chambre')], max_length=50)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('region', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('quartier', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('superficie', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='house/')),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('nb_room', models.FloatField(blank=True, max_length=15)),
                ('nb_bath', models.FloatField(blank=True, max_length=15)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
