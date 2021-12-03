import datetime, uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

from db_table.models import ProblemInfo

def problem(request):
    return render(request, "problem/problem.html")

def detail(request, problem_id):
    problem = ProblemInfo.objects.get(ProblemId = problem_id)
    print (problem_id)
    return render(request, 'problem/detail.html', {'problem': problem})