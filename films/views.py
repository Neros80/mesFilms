
from django.shortcuts import render
from films.models import Movie

def index(request):
    products = Movie.objects.all()


    return render(request, 'films/index.html', context={"products": products})
