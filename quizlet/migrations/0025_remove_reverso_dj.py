# Generated by Django 4.1.2 on 2022-10-24 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizlet', '0024_reverso_dj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reverso',
            name='dj',
        ),
    ]
