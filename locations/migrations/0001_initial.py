# Generated by Django 5.2.1 on 2025-05-08 10:55

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
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(choices=[('location', 'Location'), ('vente', 'Vente')], max_length=10)),
                ('adresse', models.CharField(max_length=255)),
                ('statut', models.CharField(choices=[('disponible', 'Disponible'), ('en_conversation', 'En conversation'), ('vendu_loue', 'Vendu/Loué')], default='disponible', max_length=20)),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
