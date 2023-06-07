from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.
class Commune(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
class Surveys(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    comuna = models.ForeignKey(Commune, on_delete=models.CASCADE)
    barrio = models.ForeignKey(District, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.name}"
class SurveyDuration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Surveys, on_delete=models.CASCADE)
    duration = models.DurationField()

    def __str__(self) -> str:
        return f"User: {self.user.username}, Survey: {self.survey.name}, Duration: {self.duration}"   
class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Surveys, on_delete=models.CASCADE)
    latitud = models.DecimalField(max_digits=20, decimal_places=8)
    longitud = models.DecimalField(max_digits=20, decimal_places=8)
    def __str__(self) -> str:
        return f"user: {self.user.username} Encuesta: {self.survey.name}"
class Questions(models.Model):
    question = models.CharField(max_length=200)
    survey = models.ForeignKey(Surveys, on_delete=models.CASCADE)
    def __str__(self)->str:
        return f"{self.question} Encuesta: {self.survey.name}"

class AnswerOptions(models.Model):
    options = models.CharField(max_length=100)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE,)
    def __str__(self) -> str:
        return f"{self.options}, pregunta: {self.question.question}"

class Answer(models.Model):
    answeroptions = models.ForeignKey(AnswerOptions, on_delete=models.CASCADE)
    questions = models.ForeignKey(Questions,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"Opcion: {self.answeroptions} Pregunta: {self.questions}"



