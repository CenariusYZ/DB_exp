import datetime, uuid
from django.shortcuts import render, redirect, get_object_or_404
import random

from db_table.models import ProblemInfo

def problem(request):
    problems_list = ProblemInfo.objects.all()
    context = {'problems': list(problems_list)}
    return render(request, "problem/problem.html", context=context)

def detail(request, problem_id):
    problem = ProblemInfo.objects.get(ProblemId = problem_id)
    problems = ProblemInfo.objects.all()
    problems = random.choices(list(problems), k=5)
    return render(request, 'problem/detail.html', {'problem': problem, 'problems': problems})