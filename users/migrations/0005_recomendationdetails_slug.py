# Generated by Django 2.2 on 2021-04-15 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210415_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='recomendationdetails',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
