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

def partenaire(request): #ici on appelle l'accueil : création de la vue
    datas['page']= 'partenaire'
    return HttpResponse(template.render(datas))

def projet(request): #ici on appelle l'accueil : création de la vue
    datas['page']= 'projet'
    return HttpResponse(template.render(datas))

def suivi(request): #ici on appelle l'accueil : création de la vue
    datas['page']= 'suivi'
    return HttpResponse(template.render(datas))

def login(request): #ici on appelle l'accueil : création de la vue
    datas['page']= 'login'
    return HttpResponse(template.render(datas))

@csrf_exempt #sert a proteger le code (code de securité)

def chatbot(request):
    #il recupere les questions et reponses 
    # datas est une variable que l'on definie nous meme (on aurait pu appeller données)
    datas['questions'] ="" 
    datas['reponses']= ""
    
    #"POST" recupere le message qu'entre l'utilisateur c'est une fonction
    if request.method == 'POST':
        message = request.POST['message']
        pairs =[]
        #question_reponse il recupere dans la base des données
        for question_reponse in chatbotData.objects.all():
            question = question_reponse.questions
            reponse = question_reponse.reponses
            
            pair = [r"{}".format(question), reponse.split("|")]
            pairs.append(pair)
        
        chat= Chat(pairs, reflections)
        message_sansaccent = unicodedata.normalize('NFKD', message).encode('ASCII', 'ignore').decode('utf-8')
        result = chat.respond(message_sansaccent)

        
        #"result" et "message" est a definir dans ton index
        datas['result'] = result
        datas['message']= message
        
    datas['page']= 'chatbot'
    return HttpResponse(template.render(datas))


# def afficher_messages(messages):
#     # Initialiser une chaîne de caractères HTML contenant le formulaire
#     chatbot = """
#         <form>
#             <label for="message">Saisir un message :</label>
#             <input type="text" id="message" name="message">
#             <input type="submit" value="Envoyer">
#         </form>
#     """
#     #Ajouter chaque message à la chaîne HTML
#     for message in messages:
#         chatbot += f"<input>{message}</input>"
#      # Renvoyer la chaîne HTML complète
#     return chatbot

# ORIGINE OK

    # if request.method == 'POST':
    #     message = request.POST['message']
    #     pairs =[]
    #     #question_reponse il recupere dans la base des données
    #     for question_reponse in chatbotData.objects.all():
    #         question = question_reponse.questions
    #         reponse = question_reponse.reponses
            
    #         pair = [r"{}".format(question), reponse.split("|")]
    #         pairs.append(pair)
        
    #     chat= Chat(pairs, reflections)
    #     result = chat.respond(message)
        
    #     #"result" et "message" est a definir dans ton index
    #     datas['result'] = result
    #     datas['message']= message
        
    # datas['page']= 'chatbot'
    # return HttpResponse(template.render(datas))
    
    # # code récupéré sur chatgpt pour afficher toutes les bulles
    # def afficher_messages(messages):
    # # Initialiser une chaîne de caractères HTML contenant le formulaire
    #     chatbot = """
    #     <form>
    #         <label for="message">Saisir un message :</label>
    #         <input type="text" id="message" name="message">
    #         <input type="submit" value="Envoyer">
    #     </form>
    # """
    # #Ajouter chaque message à la chaîne HTML
    # for message in messages:
    #     chatbot += f"<p>{message}</p>"
    #  # Renvoyer la chaîne HTML complète
    # return chatbot
