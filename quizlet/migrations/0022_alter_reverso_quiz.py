# Generated by Django 4.1 on 2022-08-23 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizlet', '0021_reverso_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reverso',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quizlet.quiz'),
        ),
    ]