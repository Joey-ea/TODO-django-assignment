# Generated by Django 5.2.4 on 2025-07-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_rename_created_at_task_date_added_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="category",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="task",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="task",
            name="due_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
