# Generated by Django 4.1 on 2024-06-30 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GanesanTeam', '0017_alter_claimstracker_sellunitprice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimstracker',
            name='Ageingdays',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='claimstracker',
            name='Qty',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
