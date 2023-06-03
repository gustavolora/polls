from typing import Any
from django import http
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

class SurveyView(TemplateView):
    template_name = 'login.html'
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)


def login(request):
    if request.method == 'POST':
        user = request.POST.get['login']
        password = request.POST.get['password']


def surveys(request):
    pass

