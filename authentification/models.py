# accounts/models.py
from django.db import models
from django.contrib.auth.models import User
from house.models import Logement

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    profile_image = models.ImageField(upload_to='authentification/', blank=True)

    def __str__(self):
        return self.user.username
    class Meta:
        abstract = True

class Locataire(UserProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='locataire')
    logements = models.ManyToManyField(to=Logement, related_name='locataire')

class Proprietaire(UserProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='proprietaire')
    logements = models.ManyToManyField(to=Logement, related_name='proprietaire')
