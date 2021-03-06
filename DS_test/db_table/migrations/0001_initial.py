# Generated by Django 3.2.9 on 2021-11-09 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemInfo',
            fields=[
                ('ProblemId', models.AutoField(primary_key=True, serialize=False)),
                ('ProblemName', models.CharField(max_length=30, verbose_name='题目名称')),
                ('ProblemDiscription', models.CharField(max_length=100, verbose_name='题面描述地址')),
                ('ProblemTimeLimit', models.IntegerField(max_length=10, verbose_name='时间限制')),
                ('ProblemMemLimit', models.IntegerField(max_length=10, verbose_name='空间限制')),
            ],
            options={
                'verbose_name': '题目信息',
                'verbose_name_plural': '题目信息',
                'db_table': 'prob_Info',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20, verbose_name='用户名称')),
                ('upasswd', models.CharField(max_length=30, verbose_name='密码md5')),
                ('uschool', models.CharField(max_length=30, verbose_name='学校')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'user_info',
            },
        ),
    ]
