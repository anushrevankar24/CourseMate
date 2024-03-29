# Generated by Django 5.0 on 2024-01-01 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0004_alter_courses_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='credits',
            field=models.IntegerField(default='default_credits'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='details',
            field=models.TextField(default='default_details'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='slots',
            field=models.IntegerField(default='default_slots'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='title',
            field=models.CharField(default='default_title', max_length=150),
        ),
    ]
