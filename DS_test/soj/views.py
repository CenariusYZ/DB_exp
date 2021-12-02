import datetime, uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

def index(request):
    return render(request, "soj/index.html")