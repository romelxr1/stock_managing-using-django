# Generated by Django 4.2 on 2025-07-08 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_materiel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='commercial',
        ),
        migrations.AddField(
            model_name='lignedecommande',
            name='prix_unitaire',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
