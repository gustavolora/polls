from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Surveys(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    def __str__(self) -> str:
        return f"{self.name}"

class Questions(models.Model):
    question = models.CharField(max_length=200)
    survey = models.ForeignKey(Surveys, on_delete=models.CASCADE)
    def __str__(self)->str:
        return f"{self.question} Encuesta: {self.survey.name}"

class AnswerOptions(models.Model):
    options = models.CharField(max_length=100)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE,)
    def __str__(self) -> str:
        return f"{self.options}, pregunta: {self.question.id}"

class Answer(models.Model):
    answeroptions = models.ForeignKey(AnswerOptions, on_delete=models.CASCADE)
    questions = models.ForeignKey(Questions,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"Opcion: {self.answeroptions} Pregunta: {self.questions}"

