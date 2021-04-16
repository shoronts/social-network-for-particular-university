# Generated by Django 2.2 on 2021-04-15 20:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210411_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='recomendationDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('full_name', models.CharField(max_length=100)),
                ('university_of_graduation', models.CharField(max_length=100)),
                ('department_and_major', models.CharField(max_length=100)),
                ('graduations_degree', models.CharField(max_length=100)),
                ('grade_and_gpa', models.CharField(max_length=100)),
                ('studies_student_wishes_to_pursue', models.CharField(max_length=100)),
                ('specialization_in_higher_studies', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('academic_excellence', models.CharField(max_length=100)),
                ('initiavive_and_motivation', models.CharField(max_length=100)),
                ('expreeing_ideas', models.CharField(max_length=100)),
                ('critical_thinking', models.CharField(max_length=100)),
                ('ability_to_accept_and_utilize_criticism', models.CharField(max_length=100)),
                ('self_confidence_and_responsibility', models.CharField(max_length=100)),
                ('ability_to_plan_and_execute_research', models.CharField(max_length=100)),
                ('acquiring_research_technique', models.CharField(max_length=100)),
                ('creative_and_originality', models.CharField(max_length=100)),
                ('linguistic_ikills', models.CharField(max_length=100)),
                ('general_knowledge', models.CharField(max_length=100)),
                ('overall_evaluation', models.CharField(max_length=100)),
                ('note_about_the_applicant', models.CharField(max_length=100)),
                ('faculty_dean_name', models.CharField(max_length=100)),
                ('faculty_dean_signature', models.CharField(max_length=100)),
                ('faculty_dean_date', models.CharField(max_length=100)),
                ('recommenders_name', models.CharField(max_length=100)),
                ('academic_position', models.CharField(max_length=100)),
                ('academic_department', models.CharField(max_length=100)),
            ],
        ),
    ]