# Generated by Django 2.2.4 on 2022-02-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_auto_20220201_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='universal',
            name='ans',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
