# Generated by Django 4.0.4 on 2022-05-24 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='daily_rate',
            field=models.FloatField(default=True),
        ),
    ]
