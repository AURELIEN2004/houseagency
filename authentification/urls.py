# accounts/urls.py
# accounts/urls.py

from django.urls import path
from .views import register, login_view, account, logout_view, delete_account,profile,hase,edit

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('edit/', edit, name='edit'),  
    path('logout/', logout_view, name='logout'),
    path('delete/', delete_account, name='delete_account'),

    path('o', account, name='account'),
    path('', profile, name='profile'),
    path('', hase, name='hase'),

]    