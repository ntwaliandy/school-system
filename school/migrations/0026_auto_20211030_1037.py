# Generated by Django 3.0.5 on 2021-10-30 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0025_auto_20211030_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grading',
            name='course_unit',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='grading',
            name='roll',
            field=models.CharField(max_length=50),
        ),
    ]
