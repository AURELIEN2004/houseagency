from django.db import models
from django.contrib.auth.models import AbstractUser

class Logement(models.Model):
    CATEGORIES = [
        ('appartement', 'Appartement'),
        ('maison', 'Maison'),
        ('studio', 'Studio'),
        ('chambre', 'Chambre'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORIES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    area = models.PositiveIntegerField()
    image = models.URLField(blank=True)
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
       ordering = ['-date_added']  

    def __str__(self):
        return f"{self.category} à {self.city} quatier : {self.neighborhood} - {self.area} m²  {self.description}"
                                                                                      


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    

    def __str__(self):
        return self.username
