# Generated by Django 5.1.2 on 2024-10-16 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0002_league_alter_competition_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='coefficient',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
