# Generated by Django 3.1.7 on 2021-04-14 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizes', '0007_auto_20210414_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='option',
            field=models.CharField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')], max_length=2),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=120),
        ),
    ]
