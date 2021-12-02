import datetime, uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

import sys
sys.path.append('..')
from db_table.models import UserInfo

def verify_account(username, school, password1, password2) -> str:
    if password1 != password2:
        return '两次输入的密码不相同'
    if len(password1) < 6 or len(password1) > 20:
        return '密码的长度不应小于6，大于20'
    if UserInfo.objects.filter(user_name = username, is_active = True).exists():
        return '用户名[{}]已被注册'.format(username)
    return ''

def register(request):
    if request.user.is_authenticated:
        return redirect('/') # 登录状态下无法注册
    if request.method == "GET":
        return render(request, "userinfo/register.html")
    elif request.method == "POST":
        request_username = request.POST.get('username', '').strip()
        request_school = request.POST.get('school', '').strip()
        request_password1 = request.POST.get('password1', '').strip()
        request_password2 = request.POST.get('password2', '').strip()
        message = verify_account(request_username, request_school, request_password1, request_password2)
        
        if len(message) == 0:
            try:
                UserInfo.objects.create(
                    user_name = request_username,
                    uschool = request_school,
                    is_active = True,
                    upasswd = make_password(request_password1)
                )

                message = '注册成功，前往登录界面！'             #####修改
                print ('???')
                return render(request, "userinfo/login.html")
            except:
                print ('!!!')
                return render(request, "userinfo/register.html")

        
        messages.success(request, 'Hello world.')
        return render(request, "userinfo/register.html")


def login(request):
    print (request.user.is_authenticated)
    if request.user.is_authenticated:
        print(request.user.id)
        return redirect('/') # 无法重复登录
    if request.method == "GET":
        return render(request, "userinfo/login.html")
    elif request.method == "POST":

        
        '''username = request.POST.get('name', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        print (user)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return render(request, "userinfo/login.html")
        else:
            return render(request, "userinfo/login.html")'''

        request_user = request.POST.get('name', '').strip()
        request_password = request.POST.get('password', '').strip()
        user = None
        message = ''
        print (request_user)
        try:
            user = UserInfo.objects.get(user_name = request_user, is_active = True)
            if not check_password(request_password, user.upasswd):
                message = '密码错误'
        except:
            message = '用户名不存在，请前往注册或进行邮箱认证'

        print (message)
        print (user)
        #user = auth.authenticate(username = request_user, password = make_password(request_password))
        if message == '':
            auth.login(request, user)
            return redirect('/profile')
        else:
            return render(request, "userinfo/login.html", {'message': message})


def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    return render(request, "userinfo/profile.html")