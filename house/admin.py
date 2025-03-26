from django.contrib import admin
#from .models import Utilisateur
# Register your models here.


from .models import Logement

# Register your models here.
class AdminLogement(admin.ModelAdmin):
    list_display = ('categorie', 'prix','region','ville','quartier','superficie','phone','nb_room','nb_bath','date_added')

admin.site.register(Logement, AdminLogement)