from django.db import models

# Create your models here.
"""
Films
    - Titre du film
    - Date de sortie (Mois:Année)   
    - Realisateur
    - Synopsis

"""

class Product(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateField
    director = models.CharField(max_length=128)
    synopsis = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.title