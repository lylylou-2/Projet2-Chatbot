from django.shortcuts import render #ajout pour la création de la vue
from django.http import HttpResponse
from django.template import loader #ajout pour la gestion des templates
from chatbot.models import chatbotData
import nltk
from nltk.chat.util import Chat, reflections
from django.views.decorators.csrf import csrf_exempt

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


template = loader.get_template('index.html')
datas= {'page':'home',
		'nav' : [
			{'label':'home', 'href':''},
			{'label':'formulaire', 'href':'formulaire'},
			{'label':'chatbot', 'href':'chatbot'},
		]
	}

def home(request): #ici on appelle l'accueil : création de la vue
    datas['page']= 'home'
    return HttpResponse(template.render(datas))

def projet(request): #ici on appelle l'accueil : création de la vue
    datas['page']= 'projet'
    return HttpResponse(template.render(datas))


@csrf_exempt
def chatbot(request):
    datas['questions'] ="" 
    datas['reponses']= ""
    
    if request.method == 'POST':
        message = request.POST['message']
        pairs =[]
        for question_reponse in chatbotData.objects.all():
            question = question_reponse.questions
            reponse = question_reponse.reponses
            
            pair = [r"{}".format(question), reponse.split("|")]
            pairs.append(pair)
        
        chat= Chat(pairs, reflections)
        result = chat.respond(message)
        
        datas['result'] = result
        datas['message']= message
        
    datas['page']= 'chatbot'
    return HttpResponse(template.render(datas))

        
# def get_response(questions):
#     trainings = chatbotData.objects.all()
#     reponses = "Déso j'ai pas compris"
#     for question in trainings:
#         if question.questions in questions:
#             reponses = question.reponses
#             break
#     return reponses

        


#faire les autres vues pour toutes les pages


# def chatbot(request):
#     data ={'message' : '', 'question': ''}
#     if request.method == 'POST':
#         questions = request.POST['questions']
#         reponses = get_response(questions)
#         data ={'message' : reponses, 'question': questions}
#         #return JsonResponse({'reponses': reponses})
#     template=loader.get_template("chatbot.html")
#     return HttpResponse(template.render(data))

# def get_response(questions):
#     trainings = chatbotData.objects.all()
#     question_list = [q.questions.lower() for q in trainings]
#     if questions.lower() in question_list:
#         q = trainings.filter(questions__iexact=questions).first()
#         return q.reponses
#     else:
#         return "?? " + questions.lower()

