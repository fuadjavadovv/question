# Generated by Django 4.1 on 2022-08-27 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizlet', '0022_alter_reverso_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizs', to='quizlet.quiz'),
        ),
    ]
