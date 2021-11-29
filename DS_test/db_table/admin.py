from django.contrib import admin
from db_table import models

# Register your models here.
admin.site.register(models.UserInfo)
admin.site.register(models.ProblemInfo)
admin.site.register(models.AttemptsInfo)
admin.site.register(models.MatchInfo)
admin.site.register(models.User_Match_Info)
admin.site.register(models.Problem_Match_Info)