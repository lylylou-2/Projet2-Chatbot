from django.shortcuts import render #ajout pour la création de la vue
from django.http import HttpResponse
from django.template import loader #ajout pour la gestion des templates
from chatbot.models import chatbotData
import nltk
from nltk.chat.util import Chat, reflections
from django.views.decorators.csrf import csrf_exempt
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import FrenchStemmer
import unicodedata
import json
import ast


#le template appelle la structure du site (meme nav,footer,css)
template = loader.get_template('index.html')
datas= {'page':'home',
		'nav' : [
			{'label':'home', 'href':''},
			{'label':'formulaire', 'href':'formulaire'},
			{'label':'chatbot', 'href':'chatbot'},
		]
	}

#le def ici sert a definir toutes les pages (il faut modifier les pages URLS(path=chemin) et index(if et endif) pour que tout fonctionne) 
def home(request): #ici on appelle l'accueil : création de la vue
    #"page" est definie ds l'index
    datas['page']= 'home'
    return HttpResponse(template.render(datas))

def partenaire(request): #ici on appelle la page partenaire : création de la vue
    datas['page']= 'partenaire'
    return HttpResponse(template.render(datas))

def projet(request): #ici on appelle la page projet : création de la vue
    datas['page']= 'projet'
    return HttpResponse(template.render(datas))

def suivi(request): #ici on appelle la page suivi : création de la vue
    datas['page']= 'suivi'
    return HttpResponse(template.render(datas))

def login(request): #ici on appelle la page connexion : création de la vue
    datas['page']= 'login'
    return HttpResponse(template.render(datas))

def contact(request): #ici on appelle la page contact : création de la vue
    datas['page']= 'contact'
    return HttpResponse(template.render(datas))


@csrf_exempt #sert a proteger le code (code de securité)


def chatbot(request):
    #il recupere les questions et reponses
    datas['history']= []
    # datas est une variable que l'on definit nous meme (on aurait pu appeller données)
    #"POST" recupere le message qu'entre l'utilisateur c'est une fonction
    if request.method == 'POST':
        message = request.POST['message']
        # on récupére l'historique des messages si il y en a un dans la page
        texthistory = request.POST['history']
        if (texthistory):
            json_dat = json.dumps(ast.literal_eval(texthistory))
            datas['history'] = json.loads(json_dat)
        pairs =[]
        #question_reponse il recupere dans la base des données
        for question_reponse in chatbotData.objects.all():
            question = question_reponse.questions
            reponse = question_reponse.reponses
            pair = [r"{}".format(question), reponse.split("|")]
            pairs.append(pair)
        chat= Chat(pairs, reflections)
        message_sansaccent = unicodedata.normalize('NFKD', message).encode('ASCII', 'ignore').decode('utf-8')
        reponse = chat.respond(message_sansaccent)
        # ça génère les réponses et on conserve les échange dans l'historique
        msgUser = {"type" : "user", "content": message}
        datas['history'].append(msgUser)
        if (reponse):
            msgBot = {"type" : "bot", "content": reponse}
        else:
            msgBot = {"type" : "bot", "content": "Je suis désolé, je n'ai pas compris la question. Vous pouvez reformuler la question si vous voulez ou contacter l'équipe :-("}
        datas['history'].append(msgBot)
    datas['page']= 'chatbot'
    return HttpResponse(template.render(datas))

