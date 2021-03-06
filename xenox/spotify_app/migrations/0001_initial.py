# Generated by Django 2.0.5 on 2018-06-29 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=0, max_length=25, null=True)),
                ('artist', models.CharField(blank=True, default=0, max_length=25, null=True)),
                ('image', models.CharField(blank=True, default=0, max_length=50, null=True)),
                ('releaseDate', models.CharField(blank=True, default=0, max_length=25, null=True)),
                ('genre', models.CharField(blank=True, default=0, max_length=25, null=True)),
            ],
        ),
    ]
