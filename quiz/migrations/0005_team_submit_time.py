# Generated by Django 2.2.4 on 2022-01-29 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20220129_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
