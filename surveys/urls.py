from django.urls import path
from .views import LoginView
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import CsrfViewMiddleware


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('index/', views.index, name='index'),
    path('surveys/', views.surveys, name='surveys'),
    path('surveys/survey_detail/<int:survey_id>/', views.surveydetail, name='surveydetail'),
    path('surveys/list_users/', views.listpollsters, name='listpollsters'),
    path('surveys/save_answers', views.saveAnswers, name='save_answers'),
    path('surveys/survey_detail/list_district/', views.getDistrict, name='district_list' ),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
