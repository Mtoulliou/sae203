"""

Nom ......... : urls.py
Role ........ : récupère l'url du navigateur et redirige vers la fonction voulu dabs le fichier views.py.
                
Auteur ...... : Nathan Renieville & Mattéo Toulliou
Version ..... : V1.0 du 06/04/2024

Contact : nathan.renieville@etu.umontpellier.fr
          matteo.toulliou@etu.umontpellier.fr
"""


"""
URL configuration for TCP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name = "accueil"),
    path('accueil/', views.accueil, name = "accueil"),
    path('expediteur/', views.expediteur, name = "expediteur"),
    path ('delete/<int:id>/', views.delete_colis, name = "delete_colis"),
    path('destinataire/', views.destinataire, name = "destinataire"),
    path('transporteur/', views.transporteur, name = "transporteur"),
    path('recherche/', views.recherche_colis, name='recherche_colis'),
    path('register/', views.register),
    path('log_in/', views.log_in, name='log_in_page'),
    path('log_out/', views.log_out, name='log_out'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('attribuer_transporteur/', views.attribuer_transporteur, name='attribuer_transporteur'),
    path('vehicule/', views.vehicule, name='vehicule'), 
    path('attribuer_colis/', views.attribuer_colis, name='attribuer_colis'),
    path('colis_arrive/', views.colis_arrive, name='colis_arrive'),
    path('colis_depart/', views.colis_depart, name='colis_depart'),
    path('colis_livre/', views.colis_livre, name='colis_livre'),
    path('colis_recu/', views.colis_recu, name='colis_recu'),
]
