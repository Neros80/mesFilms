from django.contrib import admin

from films.models import Movie, Country, Hall, Studio

# Register your models here.
admin.site.register(Movie)
admin.site.register(Country)
admin.site.register(Hall)
admin.site.register(Studio)