
from django.shortcuts import render
from films.models import Product

def index(request):
    products = Product.objects.all()


    return render(request, 'films/index.html', context={"products": products})
