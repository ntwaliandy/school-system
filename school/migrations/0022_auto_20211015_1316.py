# Generated by Django 3.0.5 on 2021-10-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0021_auto_20211015_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='file',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
