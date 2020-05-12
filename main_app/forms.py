from django import forms
from .models import Bird, Sighting

# make a form based off of Bird model
class BirdForm(forms.ModelForm):
    # use Meta class
    class Meta:
        model = Bird
        fields = ['name', 'size', 'description']

    
class SightingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = Sighting
        fields = ['date', 'location', 'notes']