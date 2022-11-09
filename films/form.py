from django import forms
from .models import Country, Hall, Movie, Studio

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'slug', 'date', 'director', 'synopsis', 'thumbnail','note', 'hall', 'country', 'studio')
        
class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('name', 'code')
        
class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ('name', 'city')
        
class StudioForm(forms.ModelForm):
    class Meta:
        model = Studio
        fields = ('name', 'country')
