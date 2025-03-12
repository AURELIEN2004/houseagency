from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallerie, name='gallerie'),
    path('ajouter', views.ajouter_logement, name='ajouter_logement'),
    path('modifier/<int:pk>/', views.modifier_logement, name='modifier_logement'),
    path('supprimer/<int:pk>/', views.supprimer_logement, name='supprimer_logement'),
]