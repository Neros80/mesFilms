
from django.shortcuts import render, get_object_or_404
from .form import MovieForm

from films.models import Movie, Hall



def index(request):
    movie = Movie.objects.all()
    return render(request, 'films/index.html', context={"movies": movie})

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    return render(request, 'films/movie.html', context={"movie":movie} )

def form(request):
    halls = Hall.objects.all()
    return render(request, 'films/form.html', context={"halls":halls} )



def movie_create(request):
    form = MovieForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        form = MovieForm()
        
    return render(request, 'films/form.html', {'form':form})
    