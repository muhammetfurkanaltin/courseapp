# Generated by Django 3.1.12 on 2025-01-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20250111_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.AddField(
            model_name='course',
            name='categories',
            field=models.ManyToManyField(to='courses.Category'),
        ),
    ]
