# Generated by Django 3.0.6 on 2020-05-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='movieuserrating',
            constraint=models.UniqueConstraint(fields=('movie', 'user'), name='movie_user_unique'),
        ),
    ]