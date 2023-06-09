"""projet2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path #crée le chemin pour toutes les pages
from chatbot import views #importe la vue

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='accueil'),#définie la fonction chemin qui appelle l'accueil par defaut lors de la connexion elle s'affiche
    path('home/', views.home, name='accueil'), #définie la fonction chemin qui appelle l'accueil
    path('partenaire/', views.partenaire, name='partenaire'),#définie la fonction chemin qui appelle l'accueil
    path('suivi/', views.suivi, name='suivi'), #définie la fonction chemin qui appelle l'accueil
    path('projet/', views.projet, name='projet'),
    path('chatbot/', views.chatbot, name='chatbot'), #définie la fonction chemin qui appelle le chatbot
    path('login/', views.login, name='login'), 
    path('contact/', views.contact, name='contact'), 

]
