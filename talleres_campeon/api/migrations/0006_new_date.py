# Generated by Django 4.2.1 on 2023-05-25 03:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
