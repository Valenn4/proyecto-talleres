# Generated by Django 4.2.1 on 2023-05-26 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_new_sub_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='sub_title',
            field=models.TextField(max_length=200),
        ),
    ]
