from django.shortcuts import render #ajout pour la création de la vue
from django.http import HttpResponse 
from django.template import loader #ajout pour la gestion des templates
# Create your views here.

def chatbot(request): #ici on appelle le chatbot : création de la vue
    text="<h1>Welcome sur le Chatbot</h1>"
    return HttpResponse(text)

def home(request): #ici on appelle l'accueil : création de la vue
    template=loader.get_template('index.html') #utilisation template
    return HttpResponse(template.render())

#faire les autres vues pour toutes les pages
