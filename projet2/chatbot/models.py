from django.db import models
from django.contrib import admin

# Create your models here.

class chatbotData(models.Model): #modèle créé via une class
    questions=models.TextField()
    reponses=models.TextField()
    
def __str__(self): #pour afficher
    return self.questions
