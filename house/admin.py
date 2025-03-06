from django.contrib import admin
#from .models import Utilisateur
# Register your models here.

from .models import CustomUser
#class AdminUtilisateur(admin.ModelAdmin):
  #  list_display = ('nom','email','telephone', 'mot_de_passe')
#admin.site.register(Utilisateur, AdminUtilisateur)

from .models import Logement

# Register your models here.
class AdminLogement(admin.ModelAdmin):
    list_display = ('category', 'price', 'region','city','neighborhood','area','date_added')

admin.site.register(Logement, AdminLogement)



# Register your models here.
class AdminCustomUser(admin.ModelAdmin):
      list_display = ('id', 'username', 'email', 'phone')


admin.site.register(CustomUser, AdminCustomUser)