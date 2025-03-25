# accounts/urls.py
# accounts/urls.py

from django.urls import path
from .views import register, login_view, logout_view, delete_account,profile,edit,compte

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('edit', edit, name='edit'),  
    path('logout', logout_view, name='logout'),
    path('delete', delete_account, name='delete_account'),
    path('compte', compte, name='compte'),

    path('', profile, name='profile'),

]    