import datetime, uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
import random
import datetime

from db_table.models import MatchInfo, Problem_Match_Info, ProblemInfo

def match(request):
    matchs_list = MatchInfo.objects.all()
    context = {'matchs': list(matchs_list)}
    return render(request, "match/match.html", context=context)

    
def match_detail(request, match_id):
    match = MatchInfo.objects.get(MatchId = match_id)
    matchs = MatchInfo.objects.all()
    matchs = random.choices(list(matchs), k=5)
    problem_match_infos = Problem_Match_Info.objects.filter(Match__MatchId = match_id)
    return render(request, 'match/detail.html', {'match': match, 'matchs': matchs, 'problem_match_infos': problem_match_infos})

def add(request):
    return render(request, 'match/add.html')
    
def addmatch(request):
    match_name = request.GET.get('match_name', '').strip()
    start_time1 = request.GET.get('start_time1', '').strip()
    start_time2 = request.GET.get('start_time2', '').strip()
    end_time1 = request.GET.get('end_time1', '').strip()
    end_time2 = request.GET.get('end_time2', '').strip()
    problem_list = request.GET.get('problem_list', '').strip().split()
    if match_name == "" or start_time1 == "" or start_time2 == "" or end_time1 == "" or end_time2 == "":
        return render(request, 'match/add.html')
    start_time = datetime.datetime.strptime(start_time1 + " " + start_time2, "%Y-%m-%d %H:%M")
    end_time = datetime.datetime.strptime(end_time1 + " " + end_time2, "%Y-%m-%d %H:%M")
    try:
        created_match = MatchInfo.objects.create(
            MatchName = match_name,
            MatchStartTime = start_time,
            MatchEndTime = end_time
        )
        for problem_id in problem_list:
            geted_problem = ProblemInfo.objects.get(ProblemId = problem_id)
            Problem_Match_Info.objects.create(
                Match = created_match,
                problem = geted_problem
            )
        print ('???')
        return match(request)
    except:
        print ('!!!')
        return render(request, 'match/add.html')