# Generated by Django 4.1.7 on 2023-08-07 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignee_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.CharField(max_length=30),
        ),
    ]
