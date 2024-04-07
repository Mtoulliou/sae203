# Generated by Django 5.0.4 on 2024-04-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_alter_colis_vehicule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colis',
            old_name='numeroSuivi',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='colis',
            name='adresseLivraison',
        ),
        migrations.RemoveField(
            model_name='colis',
            name='numeroConfirmation',
        ),
        migrations.RemoveField(
            model_name='colis',
            name='typeDeConfirmation',
        ),
        migrations.RemoveField(
            model_name='colis',
            name='vehicule',
        ),
        migrations.AddField(
            model_name='colis',
            name='destination',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='colis',
            name='transporteur',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='colis',
            name='destinataire',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='colis',
            name='expediteur',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='colis',
            name='hauteur',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='colis',
            name='largeur',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='colis',
            name='longueur',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='colis',
            name='poids',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='', max_length=150),
        ),
    ]