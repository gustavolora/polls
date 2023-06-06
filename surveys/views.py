from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


class SurveyView(TemplateView):
    template_name = 'login.html'


@login_required(login_url='index')
def surveys(request):
    return render(request, 'index.html',
                        {'user': request.user})


def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        converted_username = username.lower()
        user = authenticate(
            request, username=converted_username, password=request.POST['password'])
        if user is None:
            messages.error(request,'Usuario o contraseña incorrectos')
            return render(request, 'login.html')
        else:
            login(request, user)
            return redirect('surveys')

@login_required(login_url='index')
def listpollsters(request):
    users = User.objects.all()
    return render(request, 'pollster_list.html',{'users':users})

@login_required(login_url='index')
def signout(request):
    logout(request)
    return redirect('index')
