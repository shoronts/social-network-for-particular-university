# Generated by Django 2.2 on 2021-04-15 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_recomendationdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomendationdetails',
            name='note_about_the_applicant',
            field=models.CharField(max_length=10000),
        ),
    ]
