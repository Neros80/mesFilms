
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
    
# def add_movie(request, slug):
#     if request.method == "POST":
#         #traitement du form
#         title = request.POST("title")
#         slug = request.POST("slug")
#         date = request.POST("date")
#         director = request.POST("director")
#         synopsis = request.POST("synopsis")
#         thumbnail = request.POST("thumbnail")
#         hall = request.POST("hall")
        
#     movie = get_object_or_404(Movie, slug=slug)
#     new_movie, created = Movie.objects.create(
#         title=title,
#         slug=slug,
#         date=date,
#         director=director,
#         synopsis=synopsis,
#         thumbnail=thumbnail,
#         hall=hall
#         )   
#     if created:
#         new_movie.add(new_movie)
#         new_movie.save()






# def add_movie(request):
#     if request.method == "POST":
#         #traitement du form
#         title = request.POST.get("title")
#         slug = request.POST.get("slug")
#         date = request.POST.get("date")
#         director = request.POST.get("director")
#         synopsis = request.POST.get("synopsis")
#         thumbnail = request.POST.get("thumbnail")
#         hall = request.POST.get("hall")
        
#         new_movie = Movie.objects.create(
#             title=title,
#             slug=slug,
#             date=date,
#             director=director,
#             synopsis=synopsis,
#             thumbnail=thumbnail,
#             hall=hall
#         )
#         new_movie.save()
        
#     return render(request, 'films/form.html')




# class FormView(View):
    
#     template_name = 'films/form.html'
    
#     def get(self, request, *args, **kwargs):
#         context = {"message": "hello world"}
#         return render(request, self.template_name , context)