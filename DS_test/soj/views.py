import datetime, uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

from db_table.models import ProblemInfo
import random
    
def index(request):
    problems_list = ProblemInfo.objects.all()
    problems = []
    # 随机推荐五个题目
    if len(problems_list) > 0:
        problems_list = random.choices(list(problems_list), k=4)
    for p in problems_list:
        p.ProblemDiscription = p.ProblemDiscription[:20]
        problems.append(p)
    context = {"problems": problems}
    return render(request, 'soj/index.html', context)
    