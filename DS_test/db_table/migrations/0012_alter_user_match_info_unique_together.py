# Generated by Django 3.2.9 on 2021-12-03 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_table', '0011_alter_user_match_info_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user_match_info',
            unique_together={('User', 'Match')},
        ),
    ]
