# Generated by Django 5.0 on 2024-01-12 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0009_courses_filled_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='cgpa',
            field=models.DecimalField(decimal_places=2, default=7.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_in_cart', to='Dashboard.courses'),
        ),
    ]
