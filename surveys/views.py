from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Commune, Surveys , District
from django.contrib import messages
from django.http import JsonResponse


class LoginView(TemplateView):
    template_name = 'login.html'


@login_required
def index(request):
    return render(request, 'index.html',
                {'user': request.user})


@login_required
def surveys(request):
    surveys = Surveys.objects.filter()
    if surveys is None:
        return render(request, 'surveys.html', {'error': 'No te han asignado encuestas'})
    else:
        return render(request, 'surveys.html', {'surveys': surveys})


@login_required
def surveydetail(request):
    communes = Commune.objects.filter()
    context = {
        'communes': communes
        }
    
    return render(request, 'survey_detail.html', context)

@login_required
def getDistrict(request):
    comuna_id = request.GET.get('comuna_id')
    print(comuna_id)
    # Realiza la lógica necesaria para obtener los distritos según la comuna_id
    distritos = distritos = District.objects.filter(commune_id=comuna_id).values('id', 'name')
    print(distritos)
    return JsonResponse(list(distritos), safe=False)


def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        converted_username = username.lower()
        user = authenticate(
            request, username=converted_username, password=request.POST['password'])
        if user is None:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'login.html')
        else:
            login(request, user)
            return redirect('index')


@login_required
def listpollsters(request):
    users = User.objects.all()

    return render(request, 'pollster_list.html', {'users': users})


@login_required
def signout(request):
    logout(request)
    return redirect('login')
