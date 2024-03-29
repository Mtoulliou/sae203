# Generated by Django 5.0.2 on 2024-02-15 07:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminTCP',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('mdp', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Destinataire',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('mdp', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=255)),
                ('codePostal', models.CharField(max_length=5)),
                ('ville', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=10)),
                ('tel', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Expediteur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('mdp', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=255)),
                ('codePostal', models.CharField(max_length=5)),
                ('ville', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=100)),
                ('tel', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transporteur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('mdp', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=255)),
                ('codePostal', models.CharField(max_length=5)),
                ('ville', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=10)),
                ('tel', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('localisation', models.CharField(max_length=255)),
                ('transporteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.transporteur')),
            ],
        ),
        migrations.CreateModel(
            name='Colis',
            fields=[
                ('numeroSuivi', models.AutoField(primary_key=True, serialize=False)),
                ('poids', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(999999999.99)])),
                ('longueur', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(999999999.99)])),
                ('largeur', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(999999999.99)])),
                ('hauteur', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(999999999.99)])),
                ('etat', models.CharField(choices=[('EMBALLE', 'Emballé'), ('ARRIVEE', 'Arrivée'), ('DEPART', 'Départ'), ('LIVRE', 'Livré'), ('RECU', 'Reçu')], default='EMBALLE', max_length=10)),
                ('adresseLivraison', models.CharField(max_length=255)),
                ('typeDeConfirmation', models.CharField(choices=[('AUCUNE', 'Aucune'), ('MAIL', 'Mail'), ('CODE', 'Code')], max_length=10)),
                ('numeroConfirmation', models.CharField(max_length=6)),
                ('destinataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.destinataire')),
                ('expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.expediteur')),
                ('vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.vehicle')),
            ],
        ),
    ]
