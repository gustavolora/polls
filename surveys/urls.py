from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginview, name='login'),
    path('index/', views.index, name='index'),
    # admin views
    path('adminpage/',views.adminPage,name='adminpage'),
    path('adminpage/surveys', views.adminsurveys, name='adminsurveys'),
    path('adminpage/surveys/detail/<int:survey_id>/', views.adminsurveydetail, name='adminsurveydetail'),
    # user views
    path('surveys/', views.surveys, name='surveys'),
    path('surveys/survey_detail/<int:survey_id>/', views.surveydetail, name='surveydetail'),
    path('adminpage/list_users/', views.listpollsters, name='listpollsters'),
    path('surveys/save_answers/', views.saveAnswers, name='save_answers'),
    path('surveys/survey_detail/video', views.setVideo,name='setvideo'),
    path('surveys/survey_detail/list_district/', views.getDistrict, name='district_list' ),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
