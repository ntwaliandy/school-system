# Generated by Django 4.0.3 on 2022-09-21 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0032_alter_question_a_alter_question_b_alter_question_c_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_username', models.CharField(max_length=150)),
                ('question', models.CharField(max_length=10)),
                ('mark', models.CharField(max_length=10)),
            ],
        ),
    ]
