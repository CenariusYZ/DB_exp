# Generated by Django 3.2.9 on 2021-12-03 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_table', '0010_auto_20211201_2229'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user_match_info',
            unique_together=set(),
        ),
    ]
