# Generated by Django 5.0 on 2024-01-01 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_courses_program_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='username',
            new_name='email',
        ),
    ]