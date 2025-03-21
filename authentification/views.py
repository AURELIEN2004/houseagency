# accounts/views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from django.core.files.storage import FileSystemStorage

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        
        user = User.objects.create_user(username=username, email=email, password=password)
        UserProfile.objects.create(user=user, phone=phone)
        
        login(request, user)
        return redirect('profile')
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request,"nom d'utilisateur ou mots de passe incorect")
            return redirect("login")
    return render(request, 'login.html')

@login_required
def account(request):
    user_profile = UserProfile.objects.get(user=request.user)
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
        return redirect('profile')
    return render(request, 'account.html', {'user': request.user, 'profile': user_profile})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def delete_account(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    user_profile.delete()
    user.delete()
    return redirect('register')


def hase(request):
    
    return render(request,'hase.html')
def profile(request):
    
    return render(request,'profile.html')
@login_required
def edit(request):
    user_profile = UserProfile.objects.get(user=request.user)
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
        return redirect('profile')
    return render(request, 'edit.html', {'user': request.user, 'profile': user_profile})






