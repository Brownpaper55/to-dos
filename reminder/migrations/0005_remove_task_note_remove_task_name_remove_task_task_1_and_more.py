# Generated by Django 5.0.1 on 2024-01-29 04:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0004_alter_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='NOTE',
        ),
        migrations.RemoveField(
            model_name='task',
            name='name',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_1',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_2',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_3',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_4',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_5',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_6',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_7',
        ),
        migrations.AddField(
            model_name='task',
            name='Done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='Task_body',
            field=models.TextField(default=1, max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='Title',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.DateTimeField(default=datetime.date.today),
            preserve_default=False,
        ),
    ]
