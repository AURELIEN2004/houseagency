from django.urls import path
from django import views
from recherche.views import rechercher_logement
from .views import liste_logements,recherche_logement

urlpatterns = [
    path('', recherche_logement, name='recherche_logement'),
    path('1', liste_logements , name='liste_logements'),
    path('rechercher_logement', rechercher_logement, name='rechercher_logement'),
    
]