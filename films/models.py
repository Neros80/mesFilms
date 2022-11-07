from django.urls import reverse
from django.db import models

class Hall(models.Model):
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"

class Country(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Studio(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    
    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    title = models.CharField(max_length=128)
    slug= models.SlugField(max_length=128)
    date = models.DateField(null=True, blank=True)
    director = models.CharField(max_length=128)
    synopsis = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="images", blank=True, null=True)
    actif = models.BooleanField(default=True)
    upDate = models.DateTimeField(null=True, blank=True)
    note = models.FloatField(default = 0)
    hall = models.ForeignKey(Hall, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    studio = models.ForeignKey(Studio, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("movie", kwargs={"slug": self.slug})
    