# Generated by Django 5.1.3 on 2024-11-21 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_remove_employee_task_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='task_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество задач сотрудника'),
        ),
    ]
