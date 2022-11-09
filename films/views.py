
from django.shortcuts import render, get_object_or_404
from .form import MovieForm, StudioForm, HallForm, CountryForm

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

def studio_create(request):
    form = StudioForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StudioForm()
        
    return render(request, 'films/studio.html', {'form':form})

def hall_create(request):
    form = HallForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = HallForm()
        
    return render(request, 'films/hall.html', {'form':form})

def country_create(request):
    form = CountryForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CountryForm()
        
    return render(request, 'films/country.html', {'form':form})

