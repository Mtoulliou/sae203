# Generated by Django 5.0.4 on 2024-04-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0023_auto_20240407_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colis',
            name='transporteur',
            field=models.CharField(default='', max_length=100),
        ),
    ]
