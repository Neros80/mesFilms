
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from films.models import Movie, Hall


def index(request):
    movie = Movie.objects.all(),
    return render(request, 'films/index.html', context={"movies": movie})

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    return render(request, 'films/movie.html', context={"movie":movie} )

def form(request):
    hall = Hall.objects.all()
    return render(request, 'films/form.html', context={"halls":hall} )

class FormView(View):
    
    template_name = 'films/form.html'
    
    def get(self, request, *args, **kwargs):
        context = {"message": "hello world"}
        return render(request, self.template_name , context)