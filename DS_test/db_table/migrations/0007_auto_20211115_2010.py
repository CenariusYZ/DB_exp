# Generated by Django 3.2.9 on 2021-11-15 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_table', '0006_alter_attemptsinfo_problemid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attemptsinfo',
            old_name='ProblemId',
            new_name='Problem',
        ),
        migrations.RenameField(
            model_name='attemptsinfo',
            old_name='UserId',
            new_name='User',
        ),
    ]