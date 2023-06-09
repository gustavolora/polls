from .models import Respondent, SurveyRealized, Answer, AnswerOptions, Questions, Location
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .models import Commune, Surveys, District, Questions
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.db.models import Count, Avg


class LoginView(TemplateView):
    template_name = 'login.html'

def isAdmin(user):
    return user.is_superuser

@never_cache
@login_required
def index(request):
    return render(request, 'index.html',
                  {'user': request.user})

@never_cache
@user_passes_test(isAdmin,login_url='index')
@login_required
def adminPage(request):
    return render(request, 'admin.html')



@never_cache
@login_required
def surveys(request):
    surveys = Surveys.objects.all()
    survey_data = []
    for survey in surveys:
        numero_preguntas = Questions.objects.filter(survey=survey).count()
        survey_data.append(
            {'survey': survey, 'numero_preguntas': numero_preguntas})

    if surveys is None:
        return render(request, 'surveys.html', {'error': 'No te han asignado encuestas'})
    else:
        return render(request, 'surveys.html', {'surveys_data': survey_data})
    
@never_cache
@login_required
def video(request):
    return render(request, 'video.html')

@never_cache
@login_required
def surveydetail(request,survey_id):
    communes = Commune.objects.filter()
    survey = Surveys.objects.get(id=survey_id)
    questions = Questions.objects.filter(survey=survey).prefetch_related('answeroptions_set')

    context = {
        'survey_id': survey_id,
        'communes': communes,
        'questions': questions
    }
    return render(request, 'survey_detail.html', context)

@login_required
def setVideo(request):
    return render(request, 'video.html')

@login_required
def getDistrict(request):
    comuna_id = request.GET.get('comuna_id')
    distritos = distritos = District.objects.filter(
        commune_id=comuna_id).values('id', 'name')
    return JsonResponse(list(distritos), safe=False)

@csrf_protect
@login_required
def saveAnswers(request):
    if request.method == 'POST':
        nombre = request.POST.get('name')
        telefono = request.POST.get('phone')
        direccion = request.POST.get('direccion')
        commune_id = request.POST.get('comunaSelect')
        district_id = request.POST.get('barrioSelect')
        survey_id = request.POST.get('surveys_id')
        duration = request.POST.get('duration')
        print(request.POST)

        survey = Surveys.objects.get(id=survey_id)
        respondent = Respondent(name=nombre, address=direccion, phone=telefono)
        respondent.save()
        survey_realized = SurveyRealized(user=request.user, 
                                        survey=survey,
                                        respondent=respondent,
                                        commune_id=commune_id,
                                        district_id=district_id,
                                        duration=duration
                                        )
        survey_realized.save()
        location = Location()

        for pregunta_id, respuesta_id in request.POST.items():
            if pregunta_id.isdigit() and respuesta_id.isdigit():
                pregunta = Questions.objects.get(id=int(pregunta_id))
                respuesta = AnswerOptions.objects.get(id=int(respuesta_id))
                answer = Answer(surveyrealized=survey_realized,
                                answeroptions=respuesta, questions=pregunta)
                answer.save()
        context = {
            'survey_id':survey_id
        }
        return render(request, 'video.html', context)

    return redirect('index')

@csrf_protect
def signin(request):
    if request.method == 'GET':
        print('entro aqui')
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
            if user.is_superuser:
                login(request, user)
                return redirect('adminpage')
            else:
                login(request, user)
                return redirect('index')

@never_cache
@staff_member_required
@login_required
def listpollsters(request):
    users_data = User.objects.exclude(username='admin').annotate(survey_count=Count('surveyrealized'),average_duration=Avg('surveyrealized__duration')/60).order_by('-survey_count').values('username', 'survey_count', 'average_duration')
    print(users_data)
    context= {
        'users_data':users_data
    }
    return render(request, 'pollster_list.html', context)

@never_cache
@login_required
def signout(request):
    logout(request)
    return redirect('login')
