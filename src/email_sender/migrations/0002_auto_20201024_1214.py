# Generated by Django 3.1.2 on 2020-10-24 06:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_sender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 24, 12, 14, 35, 617982)),
        ),
    ]
