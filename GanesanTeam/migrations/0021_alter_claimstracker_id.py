# Generated by Django 4.1 on 2024-07-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GanesanTeam', '0020_alter_claimstracker_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimstracker',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]