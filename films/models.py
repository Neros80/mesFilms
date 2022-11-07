from django.db import models

# Create your models here.
"""
Films
    - Titre du film
    - Date de sortie (Mois:Année)   
    - Realisateur
    - Synopsis
    - pays
    - affiche
    - actif
    - date d'ajout
    - studio
    - Cinema
    - note
    - slug

"""

"""
pays 
    - Nom
    - Code
"""

"""
Cinema 
    - Nom
    - Ville
"""

"""
studio 
    - Nom
    - pays
"""



class Product(models.Model):
    title = models.CharField(max_length=128)
    slug= models.SlugField(max_length=128)
    date = models.DateField
    director = models.CharField(max_length=128)
    synopsis = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="images", blank=True, null=True)
    pays = models.IntegerField(max_length=128)

    def __str__(self):
        return self.title