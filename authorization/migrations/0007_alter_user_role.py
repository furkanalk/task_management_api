# Generated by Django 4.2.4 on 2023-08-07 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0006_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, default='idle', max_length=50),
        ),
    ]
