# Generated by Django 2.2 on 2021-04-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_recomendationdetails_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomendationdetails',
            name='note_about_the_applicant',
            field=models.TextField(max_length=10000),
        ),
    ]
