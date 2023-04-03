PROJET 2 CREATION D'UN CHATBOT POUR BLOOM IN TWO

## Welcome! 👋

**Pour relever cet exercice, vous devez avoir des connaissances de base en HTML, CSS, PYTHON et DJANGO**

## L'exercice

Votre exercice est de construire un chatbot qui répondra à des questions autour des thèmes suivants:
-grossesse
-post-partum
-partenaire

Vos utilisateurs devraient être en mesure de :

-Avoir un chatbot fonctionnel qui réponde aux questions de la base de données qui se trouve dans le serveur de django.

## Où tout trouver

Votre tâche consiste à élaborer le projet à partir de ce projet: https://github.com/Habibata-Doucoure/Future-Moms
Vous trouverez les images sur canva 

## Construction de votre projet

N'hésitez pas à utiliser le flux de travail qui vous convient. Vous trouverez ci-dessous une suggestion de processus, mais ne vous sentez pas obligé de suivre ces étapes :

(1. Installez les outils nécessaires (comme python) et la bibliothèque NLTK à l'aide de pip intall. )
2.  Dans un terminal, naviguez vers le répertoire où on a déposé le template: taper la commande "django-admin startproject <nom_du_projet>" pour créer un nouveau projet django dans ce répertoire. Remplacez 'my project' par le nom de votre choix.
3.Créez une application Django à l'aide de la commande python manage.py startapp myapp (remplacez "myapp" par le nom de votre choix pour votre application).
3.Dans le fichier settings.py de votre projet, ajoutez le nom de votre application à la liste INSTALLED_APPS.
3 Dans le fichier urls.py de votre projet, ajoutez une vue pour afficher votre template. 
3.Dans le fichier views.py de votre application, créez une vue pour afficher votre template.
3. Il faudra faire en sorte que toutes les images de votre site s'affiche avant de commmencer le projet : utiliser les tags Django pour rendre les pages dynamiques si nécessaire.
3. Vous pouvez taper à tout moment la commande: python manage.py runserver pour voir si les pages sont bien dynamiques et observer votre avancée sur le chatbot.
3. Créer une base de données sur l'interface d'administration et définir la structure de la table pour stocker les données du chatbot, comme les questions des utilisateurs et les réponses du chatbot.
4. Ecrire les codes python nécessaires au bon fonctionnement du chatbot dans la page views. Attention, il faudrait que le chatbot affiche toutes les questions et réponses de la conversation (historique) et qu'à l'aide des imports NLTK, le travail de lemmatisation et tokénisation permette de comprendre au mieux les questions.
5. Styliser votre page html du chatbot.
5. Idéalement il faudrait rassembler toutes vos pages html sur une même page et votre css sur une même page: pour chaque page vous utiliserez cette fonction pour la débuter  {%if page == 'nom de la page' %}, affichage de la partie section de la page, puis terminer avec cette fonction :  {% endif %}. 
6. Initialisez votre projet en tant que dépôt public sur [GitHub](https://github.com/). La création d'un dépôt facilitera le partage de votre code avec la communauté si vous avez besoin d'aide. Si vous n'êtes pas sûr de savoir comment procéder, [lisez attentivement cette ressource Essayer Git](https://try.github.io/). 
7. Configurez votre dépôt pour publier votre code à une adresse web. Cela sera également utile si vous avez besoin d'aide pendant un exercice, car vous pouvez partager l'URL de votre projet avec l'URL de votre dépôt. Il y a plusieurs façons de le faire, et nous fournissons quelques recommandations ci-dessous.

## Déployer votre projet

Comme mentionné ci-dessus, il existe de nombreuses façons d'héberger votre projet gratuitement. Nous recommandons l'hébergement suivant :

- [Pages GitHub](https://pages.github.com/)


## Soumettre votre code

Soumettez votre solution via le formulaire suivant :
["Je dépose mes repos"](https://descodeuses.org/je-depose-mes-repos)

N'oubliez pas que pour obtenir un feeback et comptabiliser votre exercices dans l'évaluation, vous devez :

- déposez votre lien de repo github en public
- avoir réaliser un livrable complet
- avoir un README.md personnalisé
- avoir au moins 3 commits

## Partager votre code

Il existe plusieurs endroits où vous pouvez partager votre solution :

1. Partagez votre page de solution dans le canal **#finished-projects** de la [communauté Slack](https://www.frontendmentor.io/slack).
2. Partagez le repo et les URL en direct sur tweeter.
3. Partagez votre solution sur d'autres canaux sociaux comme LinkedIn.
4. Tenez un blog sur votre expérience d'apprentissage, vos choix techniques. Parler de votre code est un excellent moyen de renforcer ce que vous avez appris. Les plateformes idéales pour écrire sont [dev.to](https://dev.to/), [Hashnode](https://hashnode.com/) et [Medium](https://medium.com/).
