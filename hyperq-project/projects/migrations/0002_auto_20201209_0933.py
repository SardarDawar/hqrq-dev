# Generated by Django 3.1.4 on 2020-12-09 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-dt_create']},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='dt_creation',
            new_name='dt_create',
        ),
        migrations.AddField(
            model_name='project',
            name='dt_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
