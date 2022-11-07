from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from films.views import index, movie_detail
from mesFilms import settings

urlpatterns = [
    path('', index, name='index'),
    path('film/<str:slug>', movie_detail, name='movie'),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
