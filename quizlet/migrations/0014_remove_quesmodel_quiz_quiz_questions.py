# Generated by Django 4.1 on 2022-08-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizlet', '0013_quesmodel_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quesmodel',
            name='quiz',
        ),
        migrations.AddField(
            model_name='quiz',
            name='questions',
            field=models.ManyToManyField(to='quizlet.quesmodel'),
        ),
    ]
