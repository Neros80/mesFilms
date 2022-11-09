from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'slug', 'date', 'director', 'synopsis', 'thumbnail','note', 'hall', 'country', 'studio')