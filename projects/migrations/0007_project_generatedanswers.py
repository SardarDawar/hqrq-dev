# Generated by Django 3.1.4 on 2021-01-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_generatedquestionsleadingtext'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='generatedAnswers',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Project Answers'),
        ),
    ]
