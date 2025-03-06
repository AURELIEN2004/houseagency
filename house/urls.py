from django import views
from django.urls import path
from .views import *
from house.views import index, login, register,gallery,crud
from django.urls import path
from .views import profile_view, edit_profile, delete_account, user_logout,home
from django.urls import path
from .views import register, login_view,hame

urlpatterns = [
    path('add', add, name='add'),
    path('index', index, name='index'),
    path('crud', crud, name='crud'),
    path('base', base, name='base'),
    path('',home, name="home"),
    
    #path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('recherche_logement', recherche_logement, name='recherche_logement'),
    path('1', liste_logements , name='liste_logements'),
    path('gallery', gallery, name='gallery'),
    path('<int:myid>', detail, name="detail"),
    path('add/',add,name='add'),
    path('addrec/',addrec,name='addrec'),
    path('delete/<int:id>/',delete,name='delete'),
    path('update/<int:id>/',update,name='update'),
    path('update/uprec/<int:id>/',uprec,name='uprec'),
    path('<int:myid>', detail, name="detail"),

    path('register/', register, name='register'),
    path('profile/<int:id>/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('hame', hame, name='hame'),
    path('informations/', afficher_informations, name='informations'),


    
    path('edit/', edit_profile, name='edit_profile'),
    path('delete/', delete_account, name='delete_account'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),


]

