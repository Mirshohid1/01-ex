# Generated by Django 5.1.1 on 2024-09-17 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_remove_answer_question_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='subject',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.subject'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.answer'),
        ),
    ]
