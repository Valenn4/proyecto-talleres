# Generated by Django 4.2.1 on 2023-05-24 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_match_name_one_team_match_name_two_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='name_one_team',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='match',
            name='name_two_team',
            field=models.CharField(max_length=50),
        ),
    ]
