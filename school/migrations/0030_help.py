# Generated by Django 3.0.5 on 2021-11-01 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0029_auto_20211030_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('message', models.TextField(blank=True, max_length=1000)),
                ('student', models.CharField(default='student name', max_length=30, null=True)),
            ],
        ),
    ]
