from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Logement,CustomUser
from django.contrib.auth.decorators import login_required
from django.views import *
from django.shortcuts import render
from .models import Logement

from django.shortcuts import render, redirect


from .forms import CustomUserCreationForm, CustomAuthenticationForm


# Create your views here.
def crud(request):  
    logements=Logement.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
       logements= Logement.objects.filter(title__icontains=item_name)
    #paginator = Paginator(logements, 4)
    #page = request.GET.get('page')
    #logements = paginator.get_page(page)
    return render(request,'crud.html',{'logements':logements})
  
def add(request):
    return render(request,'add.html')
 
def addrec(request):
    x=request.POST['category']
    y=request.POST['price']
    z=request.POST['region']
    a=request.POST['city']
    b=request.POST['neighborhood']
    c=request.POST['description']
    d=request.POST['area']
    e=request.POST['image']
    logements=Logement(category=x,price=y,region=z, city=a, neighborhood=b, description=c, area=d, image=e)
    logements.save()
    return redirect("/")

#fonction pour supprimer
def delete(request,id):
    logements=Logement.objects.get(id=id)
    logements.delete()
    return redirect('/')
#mise a jour d un membre
def update(request,id):
    logements=Logement.objects.get(id=id)
    return render(request,'update.html',{'logements':logements})

def home(request):
    return render (request,'home.html')

def base(request):
    return render (request,'base.html')

def index(request):
    return render (request,'index.html')





def uprec(request, id):
    x=request.POST['category']
    y=request.POST['price']
    z=request.POST['region']
    a=request.POST['city']
    b=request.POST['neighborhood']
    c=request.POST['description']
    d=request.POST['area']
    e=request.POST['image']
    logements=Logement.objects.get(id=id)
    logements.category=x
    logements.price=y
    logements.region=z
    logements.city=a
    logements.neighborhood=b
    logements.description=c
    logements.area=d
    logements.image=e
    logements.save()
    return redirect("/")




def recherche_logement(request):
    if request.method == 'GET':
        category = request.GET.get('category', 'tous')
        price = request.GET.get('price', 0)
        region = request.GET.get('region', '')
        city = request.GET.get('city', '')
        neighborhood = request.GET.get('neighborhood', '')
        description = request.GET.get('description', '')
        area = request.GET.get('area', 0)

        logements = Logement.objects.all()

        if category != 'tous':
            logements = logements.filter(category=category)
        if region:
            logements = logements.filter(region__iexact=region)
        if city:
            logements = logements.filter(city__iexact=city)
        if neighborhood:
            logements = logements.filter(neighborhood__iexact=neighborhood)
        #logements = logements.filter(price__lte=price)
        #logements = logements.filter(area__gte=area)

        return render(request, 'liste_logements.html', {'logements': logements})

    return render(request, 'logements/recherche_logement.html')


def liste_logements(request):
     return render(request, 'liste_logements.html')

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



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('hame')  # Rediriger vers une page d'accueil ou autre
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile_view(request,id):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('hame')  # Rediriger vers une page d'accueil ou autre
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})
def hame(request):
    return render (request,'hame.html')

def afficher_informations(request):
    customUser = CustomUser.objects.all()
    return render(request, 'informations.html', {'customUser': customUser})


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUser(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUser(instance=user)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def delete_account(request):
    user = request.user
    user.delete()
    return redirect('home')
def home(request):
    return render(request,'home.html')

def user_logout(request):
    logout(request)
    return redirect('home')






