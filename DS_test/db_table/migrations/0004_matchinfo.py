# Generated by Django 3.2.9 on 2021-11-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_table', '0003_attemptsinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchInfo',
            fields=[
                ('MatchId', models.AutoField(primary_key=True, serialize=False)),
                ('MatchName', models.CharField(max_length=100, verbose_name='比赛名称')),
                ('MatchStartTime', models.DateTimeField(verbose_name='开始时间')),
                ('MatchEndTime', models.DateTimeField(verbose_name='结束时间')),
            ],
            options={
                'verbose_name': '比赛信息',
                'verbose_name_plural': '比赛信息',
                'db_table': 'Match_Info',
            },
        ),
    ]
