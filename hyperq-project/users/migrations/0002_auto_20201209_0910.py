# Generated by Django 3.1.4 on 2020-12-09 09:10

import common.storage
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=common.storage.OverwriteStorage(), upload_to=users.models.profileImageSavePath),
        ),
    ]
