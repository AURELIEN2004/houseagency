# views.py
from django.shortcuts import render, redirect, get_object_or_404
from house.models import Logement

from django.views import *

def rechercher_logement(request):
    logements = Logement.objects.all()
    categorie = request.GET.get('categorie', '')
    prix_min = request.GET.get('prix_min', '')
    prix_max = request.GET.get('prix_max', '')
    region = request.GET.get('region', '')
    ville = request.GET.get('ville', '')
    quartier = request.GET.get('quartier', '')
    superficie_min = request.GET.get('superficie_min', '')
    superficie_max = request.GET.get('superficie_max', '')

    if request.method == 'GET':
        if categorie != 'tous':
            logements = logements.filter(categorie=categorie)
        if prix_min:
            logements = logements.filter(prix__gte=prix_min)
        if prix_max:
            logements = logements.filter(prix__lte=prix_max)
        if region:
            logements = logements.filter(region=region)
        if ville:
            logements = logements.filter(ville=ville)
        if quartier:
            logements = logements.filter(quartier=quartier)
        if superficie_min:
            logements = logements.filter(superficie__gte=superficie_min)
        if superficie_max:
            logements = logements.filter(superficie__lte=superficie_max)
        #logements = logements.filter(prix__lte=prix__lte)
        #logements = logements.filter(area__gte=area)

    return render(request, 'liste_logements.html', {'logements': logements})



def liste_logements(request):
    logements=Logement.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
       logements= Logement.objects.filter(title__icontains=item_name)
    
    paginator = Paginator(logements, 4)
    page = request.GET.get('page')
    logements= paginator.get_page(page)
    return render(request,'gallery.html',{'logements':logements})
   
def recherche_logement(request):
    return render(request, 'recherche_logement.html')
