# Generated by Django 3.1.7 on 2021-04-17 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
