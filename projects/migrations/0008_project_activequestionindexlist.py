# Generated by Django 3.1.4 on 2021-01-16 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_generatedanswers'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='activeQuestionIndexList',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]