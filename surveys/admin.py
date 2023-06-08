from django.contrib import admin
from .models import Answer, AnswerOptions, Questions, Surveys, SurveyRealized
admin.site.register(Answer)
admin.site.register(AnswerOptions)
admin.site.register(Questions)
admin.site.register(Surveys)
admin.site.register(SurveyRealized)

