# Generated by Django 4.1 on 2022-08-18 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizlet', '0012_remove_quesmodel_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesmodel',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quizlet.quiz'),
        ),
    ]
