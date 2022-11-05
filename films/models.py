from django.db import models

# Create your models here.
"""
Films
    - Titre du film
    - Date de sortie (Mois:Année)   
    - Realisateur
    - Synopsis

"""

class Product(models.Models):
    title = models.CharFleid(max_lenght=128)
    date = models.DateField
    director = models.CharField(max_lenght=128)
    synopsis = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="images", blank=True, null=True)