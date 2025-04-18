# accounts/views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Locataire, Proprietaire
from django.core.files.storage import FileSystemStorage

def register(request):
    msg = None
    if request.method == "POST":
        typec = request.POST.get('typec')
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        profile_image = request.FILES.get('profile_image')  # Get the uploaded profile image
        
        
        if User.objects.filter(username=username).exists():
            msg = "Ce nom d'utilisateur est déjà pris."
        elif User.objects.filter(email=email).exists():
            msg = "Cet email est déjà utilisé."
        else:
            user = User.objects.create_user(username=username, email=email, password=password)

            if typec == "locataire":
                Locataire.objects.create(user=user, phone=phone, profile_image=profile_image)
            elif typec == "propriétaire":
                Proprietaire.objects.create(user=user, phone=phone, profile_image=profile_image)
            
            login(request, user)
            return redirect('home')
    return render(request, 'register.html', {'msg': msg})

def login_view(request):
    msg = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if Locataire.objects.filter(user=user).exists():
                return redirect('home')  # Redirect to locataire-specific dashboard
            elif Proprietaire.objects.filter(user=user).exists():
                return redirect('home')  # Redirect to proprietaire-specific dashboard
            else:
                return redirect('home')  # Default redirect if no specific role is found
        else:
            msg = "Nom d'utilisateur ou mot de passe incorrect"
    return render(request, 'login.html', context={'msg': msg})

@login_required
def edit(request):
    if Locataire.objects.filter(user=request.user).exists():
        user_profile = Locataire.objects.get(user=request.user)
    else:
        user_profile = Proprietaire.objects.get(user=request.user)
    if request.method == "POST":
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.username = request.POST.get('username', user.username)
        user.last_name = request.POST.get('last_name', user.last_name)

        # Gestion de la photo de profil
        if request.FILES:
            profile_image = request.FILES['profile_image']
            fs = FileSystemStorage()
            filename = fs.save(profile_image.name, profile_image)
            user_profile.profile_image = filename
        user_profile.phone = request.POST.get('phone', user_profile.phone)
        
        user.save()
        user_profile.save()
        return redirect('compte')
    return render(request, 'edit.html', {'user': request.user, 'profile': user_profile})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def delete_account(request):
    user = request.user
    user.delete()
    return redirect('register')

@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def compte(request):
    if Locataire.objects.filter(user=request.user).exists():
        user_profile = Locataire.objects.get(user=request.user)
    else:
        user_profile = Proprietaire.objects.get(user=request.user)
    return render(request, 'compte.html', {'profile': user_profile})

   




