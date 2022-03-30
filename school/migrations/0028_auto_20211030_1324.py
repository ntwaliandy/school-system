# Generated by Django 3.0.5 on 2021-10-30 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0027_grading_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grading',
            name='Tests',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='grading',
            name='exam',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='grading',
            name='total',
            field=models.DecimalField(decimal_places=2, default='0.0', max_digits=6),
        ),
    ]
