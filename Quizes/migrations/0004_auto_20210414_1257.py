# Generated by Django 3.1.7 on 2021-04-14 07:27

import Quizes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizes', '0003_auto_20210414_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='quiz_id',
            field=models.IntegerField(default=Quizes.models.unique_code_generator),
        ),
    ]
