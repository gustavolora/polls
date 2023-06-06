from django.urls import path
from .views import SurveyView
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import CsrfViewMiddleware


urlpatterns = [
    path('', SurveyView.as_view(), name='index'),
    path('surveys/', views.surveys, name='surveys'),
    path('surveys/list_users/', views.listpollsters, name='listpollsters'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
