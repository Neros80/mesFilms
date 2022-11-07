
from django.shortcuts import render, get_object_or_404
from films.models import Movie

def index(request):
    movie = Movie.objects.all()


    return render(request, 'films/index.html', context={"movies": movie})

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    return render(request, 'films/movie.html', context={"movie":movie} )