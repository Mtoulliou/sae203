# Generated by Django 5.0.2 on 2024-03-05 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_colis_destinataire_alter_colis_expediteur_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colis',
            name='numeroConfirmation',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]