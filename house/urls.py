from django import views
from django.urls import path
from .views import *
from house.views import index,gallery


urlpatterns = [
    
    path('index', index, name='index'),
    
    path('base', base, name='base'),
    path('',home, name="home"),
    
    #path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('gallery', gallery, name='gallery'),
    path('<int:myid>', detail, name="detail"),
    
    path('<int:myid>', detail, name="detail"),

   # path('informations/', afficher_informations, name='informations'),


    


]

