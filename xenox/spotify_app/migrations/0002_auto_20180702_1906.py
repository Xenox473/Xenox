# Generated by Django 2.0.5 on 2018-07-02 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='genre',
            new_name='identifier',
        ),
    ]
