from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect


class SurveyView(TemplateView):
    template_name = 'login.html'


def surveys(request):
    pass
    # if request.method == 'POST':

    #     user = authenticate(request, email=request.POST['email'],
    #                         password=request.POST['password'])
    #     print(request.POST)
    #     if user is None:
    #         return render(request, 'login.html', {
    #             'error': 'usuario o contraseña incorrecta'
    #         })
    #     else:
    #         login(request, user)
    #         return render(request, 'index.html')

    # else:
    #     return render(request, 'login.html')

    #     # username = request.POST['user']

@login_required
def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        converted_username = username.lower()
        user = authenticate(
            request, username=converted_username, password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'error': 'usuario o contraseña son incorrectos'
            })
        else:
            login(request, user)
            return render(request, 'index.html',{
                'name': request.user.username
            })


def signout(request):
    logout(request)
    return redirect('index')
