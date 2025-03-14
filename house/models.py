from django.db import models


class Logement(models.Model):
    CATEGORIES = [
        ('appartement', 'Appartement'),
        ('maison', 'Maison'),
        ('studio', 'Studio'),
        ('chambre', 'Chambre'),
    ]

    categorie = models.CharField(max_length=50, choices=CATEGORIES)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    region = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    superficie = models.PositiveIntegerField()
    image = models.ImageField(upload_to='house/')
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
       ordering = ['-date_added']  

    def __str__(self):
        return f"{self.categorie} à {self.ville} quatier : {self.quartie} - {self.superficie} m²  {self.description}"
                                                                                      


