from django.contrib import admin
#from .models import Utilisateur
# Register your models here.


from .models import Logement

# Register your models here.
class AdminLogement(admin.ModelAdmin):
    list_display = ('category', 'price', 'region','city','neighborhood','area','date_added')

admin.site.register(Logement, AdminLogement)