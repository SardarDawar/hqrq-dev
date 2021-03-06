# Generated by Django 3.1.4 on 2021-01-19 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20210119_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='answerModifier',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Answer Modifier Index List'),
        ),
        migrations.AlterField(
            model_name='project',
            name='postQuestionMessage',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Post Question Message Index List'),
        ),
    ]
