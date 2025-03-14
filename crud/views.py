from django.shortcuts import render, redirect, get_object_or_404
from house.models import Logement

def gallerie(request):
    logements = Logement.objects.all()
    return render(request, 'gallerie.html', {'logements': logements})

def ajouter_logement(request):
    if request.method == 'POST':
        categorie = request.POST['categorie']
        prix = request.POST['prix']
        region = request.POST['region']
        ville = request.POST['ville']
        quartier = request.POST['quartier']
        description = request.POST['description']
        superficie = request.POST['superficie']
        image = request.FILES['image']
        
        Logement.objects.create(
            categorie=categorie,
            prix=prix,
            region=region,
            ville=ville,
            quartier=quartier,
            description=description,
            superficie=superficie,
            image=image
        )
        return redirect('gallerie')
    return render(request, 'ajouter_logement.html')

def modifier_logement(request, pk):
    logement = get_object_or_404(Logement, pk=pk)
    if request.method == 'POST':
        logement.categorie = request.POST['categorie']
        logement.prix = request.POST['prix']
        logement.region = request.POST['region']
        logement.ville = request.POST['ville']
        logement.quartier = request.POST['quartier']
        logement.description = request.POST['description']
        logement.superficie = request.POST['superficie']
        if 'image' in request.FILES:
            logement.image = request.FILES['image']
        logement.save()
        return redirect('gallerie')
    
    return render(request, 'modifier_logement.html', {'logement': logement})

def supprimer_logement(request, pk):
    logement = get_object_or_404(Logement, pk=pk)
    if request.method == 'POST':
        logement.delete()
        return redirect('gallerie')
    return render(request, 'supprimer_logement.html', {'logement': logement})
