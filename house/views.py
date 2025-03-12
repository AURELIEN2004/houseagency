from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from django.contrib import messages


from django.views import *
from django.shortcuts import render
from .models import Logement

from django.shortcuts import render, redirect





# Create your views here.

 

#fonction pour supprimer


def home(request):
    return render (request,'home.html')

def base(request):
    return render (request,'base.html')

def index(request):
    return render (request,'index.html')










def gallery(request):
    logements=Logement.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
       logements= Logement.objects.filter(title__icontains=item_name)
    
    paginator = Paginator(logements, 4)
    page = request.GET.get('page')
    logements= paginator.get_page(page)
    return render(request,'gallery.html',{'logements':logements})
   

def detail(request, myid):
    logements = Logement.objects.get(id=myid)
    return render(request, 'detail.html', {'logement': logements}) 






