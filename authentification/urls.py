# accounts/urls.py
# accounts/urls.py

from django.urls import path
from .views import register, login_view, account, logout_view, delete_account,profile,hase,edit

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('f', account, name='account'),
    path('logout/', logout_view, name='logout'),
    path('delete/', delete_account, name='delete_account'),

    path('', profile, name='profile'),
    path('d', hase, name='hase'),
    path('edit/', edit, name='edit'),
]