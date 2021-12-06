import datetime, uuid
from django.shortcuts import render, redirect
import random
import django.contrib.auth as auth

from attempts.views import attempts_page
from db_table.models import ProblemInfo, AttemptsInfo, UserInfo

def problem(request):
    problems_list = ProblemInfo.objects.all()
    context = {'problems': list(problems_list)}
    return render(request, "problem/problem.html", context=context)

def detail(request, problem_id):
    problem = ProblemInfo.objects.get(ProblemId = problem_id)
    problems = ProblemInfo.objects.all()
    problems = random.choices(list(problems), k=5)
    return render(request, 'problem/detail.html', {'problem': problem, 'problems': problems})

def submit(request, problem_id):
    problem = ProblemInfo.objects.get(ProblemId = problem_id)
    return render(request, 'problem/submit.html', {'problem': problem})

def submit_code(request, problem_id):
    problem = ProblemInfo.objects.get(ProblemId = problem_id)
    if request.method == "GET":
        print("Bad method")
        return render(request, 'problem/submit.html', {'problem': problem})
    user = request.user
    print(request.POST["code"])
    if isinstance(user, auth.models.AnonymousUser):
        return redirect(detail, problem_id)
    return redirect(attempts_page, problem.ProblemName, 1)