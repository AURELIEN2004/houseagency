from django.contrib import admin

from authentification.models import Locataire, Proprietaire

# Register your models here.

admin.site.register(Locataire)
admin.site.register(Proprietaire)