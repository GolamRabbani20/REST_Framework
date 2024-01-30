# Generated by Django 4.2.6 on 2023-11-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataScience_app', '0002_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentInfo_DataScience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('student_name', models.CharField(max_length=25)),
                ('student_dept', models.CharField(max_length=20)),
                ('course_id', models.CharField(max_length=10)),
            ],
        ),
    ]