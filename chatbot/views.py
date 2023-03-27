from django.shortcuts import render #ajout pour la création de la vue
from django.http import HttpResponse
from django.template import loader #ajout pour la gestion des templates
from django.http import JsonResponse
from .models import chatbotData
import nltk
from nltk.chat.util import Chat, reflections

# Create your views here.
# pairs = [
#     # Ajoutez ici les paires de motifs et de réponses que vous souhaitez utiliser pour votre chatbot
#     [
#         r"Bonjour",
#         ["Salut!", "Bonjour", "Comment ça va ?"]
#     ],
#     [
#         r"",
#         ["", "", ""]
#     ],
#     [
#         r"",
#         ["", ""]
#     ],
#     [
#         r"",
#         ["", ""]
#     ],
# ]

 

# chatbot = Chat(pairs, reflections)

# def chatbot(request): #ici on appelle le chatbot : création de la vue

#     text="<h1>Welcome sur le Chatbot</h1>"

#     if request.method == 'POST':
#         questions = request.POST.get('questions')
#         reponses = chatbot.respond(questions)
#         return JsonResponse({'reponses': reponses})
#     else:
#             return render(request, 'chatbot.html')

#     return HttpResponse(text)


from django.views.decorators.csrf import csrf_exempt
import random

@csrf_exempt
def chatbot(request):
    data ={'message' : '', 'question': ''}
    if request.method == 'POST':
        questions = request.POST['questions']
        reponses = get_response(questions)
        data ={'message' : reponses, 'question': questions}
        #return JsonResponse({'reponses': reponses})
    template=loader.get_template("chatbot.html")
    return HttpResponse(template.render(data))

def get_response(questions):
    trainings = chatbotData.objects.all()
    question_list = [q.questions.lower() for q in trainings]
    if questions.lower() in question_list:
        q = trainings.filter(questions__iexact=questions).first()
        return q.reponses
    else:
        return "?? " + questions.lower()


# def get_response(questions):
#     trainings = chatbotData.objects.all()
#     reponses = "Déso j'ai pas compris"
#     for question in trainings:
#         if question.questions in questions:
#             reponses = question.reponses
#             break
#     return reponses

        

def home(request): #ici on appelle l'accueil : création de la vue
    template=loader.get_template('index.html') #utilisation template
    return HttpResponse(template.render())

#faire les autres vues pour toutes les pages