# Generated by Django 4.2.4 on 2023-08-07 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0007_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(default='idle', max_length=50),
        ),
    ]
