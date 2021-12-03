from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserInfo(AbstractUser):
    UserId = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20, verbose_name="用户名称")
    upasswd = models.CharField(max_length=30, verbose_name="密码md5")
    uschool = models.CharField(max_length=30, verbose_name="学校")

    class Meta:
        db_table = 'user_info'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name


class ProblemInfo(models.Model):
    ProblemId = models.AutoField(primary_key=True)
    ProblemName = models.CharField(max_length=30, verbose_name="题目名称")
    ProblemDiscription = models.CharField(max_length=100, verbose_name="题面描述地址")
    ProblemTimeLimit = models.IntegerField(verbose_name="时间限制")
    ProblemMemLimit = models.IntegerField(verbose_name="空间限制")

    class Meta:
        db_table = "prob_Info"
        verbose_name = "题目信息"
        verbose_name_plural = "题目信息"

    def __str__(self):
        return self.ProblemName


class AttemptsInfo(models.Model):
    AttemptID = models.AutoField(primary_key=True)
    User = models.ForeignKey('UserInfo', verbose_name="用户ID", on_delete=models.CASCADE)
    Problem = models.ForeignKey('ProblemInfo', verbose_name="题目ID", on_delete=models.CASCADE)
    SourceCode = models.CharField(max_length=100000, verbose_name="源代码")
    TestResult = models.CharField(max_length=100, verbose_name="测试结果")
    TimeCost = models.IntegerField(verbose_name="使用时间")
    MemCost = models.IntegerField(verbose_name="使用空间")
    AttemptTime = models.DateTimeField(verbose_name="提交时间")

    class Meta:
        db_table = "attempt_Info"
        verbose_name = "提交信息"
        verbose_name_plural = "提交信息"

    def __str__(self):
        return str(self.User)


class MatchInfo(models.Model):
    MatchId = models.AutoField(primary_key=True)
    MatchName = models.CharField(max_length=100, verbose_name="比赛名称")
    MatchStartTime = models.DateTimeField(verbose_name="开始时间")
    MatchEndTime = models.DateTimeField(verbose_name="结束时间")

    class Meta:
        db_table = "Match_Info"
        verbose_name = "比赛信息"
        verbose_name_plural = "比赛信息"

    def __str__(self):
        return self.MatchName


class User_Match_Info(models.Model):
    User = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    Match = models.ForeignKey('MatchInfo', on_delete=models.CASCADE)

    class Meta:
        unique_together=("User", "Match")
        db_table = "User_Match"
        verbose_name = "比赛人员"
        verbose_name_plural = "比赛人员"

    def __str__(self):
        return str(self.Match) + str(self.User)


class Problem_Match_Info(models.Model):
    Match = models.ForeignKey('MatchInfo', on_delete=models.CASCADE)
    problem = models.ForeignKey('ProblemInfo', on_delete=models.CASCADE)

    class Meta:
        db_table = "Problem_Match"
        verbose_name = "比赛题目"
        verbose_name_plural = "比赛题目"

    def __str__(self):
        return str(self.Match) + str(self.problem)