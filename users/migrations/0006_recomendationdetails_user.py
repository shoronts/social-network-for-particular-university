# Generated by Django 2.2 on 2021-04-15 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_recomendationdetails_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='recomendationdetails',
            name='user',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
