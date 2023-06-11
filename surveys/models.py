from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Commune(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Surveys(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"


class Respondent(models.Model):
    name = models.CharField( max_length=60)
    address = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    recomendations = models.TextField(null=True)


class SurveyRealized(models.Model):
    user = models.ForeignKey(User,null=False, on_delete=models.CASCADE)
    survey = models.ForeignKey(Surveys,null=False, on_delete=models.CASCADE)
    respondent = models.ForeignKey(Respondent,null=False, on_delete=models.CASCADE)
    commune = models.ForeignKey(Commune, null=False, on_delete=models.CASCADE)
    district = models.ForeignKey(District, null=False,on_delete=models.CASCADE )
    duration = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"User: {self.user.username}, Survey: {self.survey.name}, Duration: {self.duration}"


class Location(models.Model):
    surveyrealized = models.ForeignKey(SurveyRealized, null=False, on_delete=models.CASCADE)
    latitud = models.DecimalField(max_digits=20, decimal_places=13, null=True,default=None)
    longitud = models.DecimalField(max_digits=20, decimal_places=13,null=True, default=None)

    def __str__(self) -> str:
        return f"user: {self.user.username}"


class Questions(models.Model):
    question = models.CharField(max_length=200)
    survey = models.ForeignKey(Surveys, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.question} Encuesta: {self.survey.name}"


class AnswerOptions(models.Model):
    options = models.CharField(max_length=100)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE,)

    def __str__(self) -> str:
        return f"opcion: {self.options}, pregunta: {self.question.question}"


class Answer(models.Model):
    surveyrealized = models.ForeignKey(SurveyRealized,null=False, on_delete=models.CASCADE)
    answeroptions = models.ForeignKey(AnswerOptions,null=False, on_delete=models.CASCADE)
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Opcion: {self.answeroptions} Pregunta: {self.questions}"
