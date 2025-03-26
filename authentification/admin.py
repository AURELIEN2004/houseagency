from django.contrib import admin
from .models import UserProfile, Locataire, Proprietaire

# Pour Locataire
@admin.register(Locataire)
class LocataireAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone','profile_image')
    search_fields = ['user__username', 'phone','typec']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')

# Pour Proprietaire
@admin.register(Proprietaire)
class ProprietaireAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone','profile_image')
    search_fields = ['user__username', 'phone','typec']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
