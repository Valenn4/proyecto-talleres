# Generated by Django 4.2.1 on 2023-05-30 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_alter_match_result_one_team_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="match", name="date", field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="match", name="time", field=models.TimeField(null=True),
        ),
    ]