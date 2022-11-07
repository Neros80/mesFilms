from django.urls import reverse
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=128)
    slug= models.SlugField(max_length=128)
    date = models.DateField
    director = models.CharField(max_length=128)
    synopsis = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="images", blank=True, null=True)
    actif = models.BooleanField(default=True)
    upDate = models.DateTimeField
    note = models.FloatField(default = 0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("movie", kwargs={"slug": self.slug})
    


class Country(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    countryName = models.CharField(max_length=128)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.movie.title} ({self.code})"

class Hall(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    hallName = models.CharField(max_length=128)
    city = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.movie.title} ({self.hallName})"

class Studio(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    studioName = models.CharField(max_length=128)
    studioCuntry = models.CharField(max_length=128)
    
    def __str__(self):
        return f"{self.movie.title} ({self.studioName})"