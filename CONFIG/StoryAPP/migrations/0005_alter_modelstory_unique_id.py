# Generated by Django 4.0.2 on 2022-02-09 18:45

import StoryAPP.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoryAPP', '0004_alter_modelstory_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelstory',
            name='unique_id',
            field=models.CharField(default=StoryAPP.models.create_new_ref_number, max_length=35, unique=True),
        ),
    ]
