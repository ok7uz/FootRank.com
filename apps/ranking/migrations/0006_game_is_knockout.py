# Generated by Django 5.1.2 on 2024-10-16 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0005_game_away_points_change_game_home_points_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_knockout',
            field=models.BooleanField(default=False),
        ),
    ]
