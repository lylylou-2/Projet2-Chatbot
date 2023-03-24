from django.shortcuts import render #ajout pour la création de la vue
from django.http import HttpResponse 
from django.template import loader #ajout pour la gestion des templates
from django.http import JsonResponse
import nltk
from nltk.chat.util import Chat, reflections


# Create your views here.
pairs = [
    # Ajoutez ici les paires de motifs et de réponses que vous souhaitez utiliser pour votre chatbot
    [
        r"Bonjour",
        ["Salut!", "Bonjour", "Comment ça va ?"]
    ],
    [
        r"",
        ["", "", ""]
    ],
    [
        r"",
        ["", ""]
    ],
    [
        r"",
        ["", ""]
    ],
]

chatbot = Chat(pairs, reflections)



def chatbot(request): #ici on appelle le chatbot : création de la vue
    text="<h1>Welcome sur le Chatbot</h1>"
    if request.method == 'POST':
        questions = request.POST.get('questions')
        reponses = chatbot.respond(questions)
        return JsonResponse({'questions': reponses})
    else:
            return render(request, 'chatbot.html')

    return HttpResponse(text)

def home(request): #ici on appelle l'accueil : création de la vue
    template=loader.get_template('index.html') #utilisation template
    return HttpResponse(template.render())

#faire les autres vues pour toutes les pages
