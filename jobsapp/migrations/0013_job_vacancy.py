# Generated by Django 4.0.1 on 2022-10-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0012_job_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
    ]
