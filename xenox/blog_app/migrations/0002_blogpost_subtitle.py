# Generated by Django 2.0.5 on 2018-07-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='subtitle',
            field=models.CharField(blank=True, default=0, max_length=25, null=True),
        ),
    ]
