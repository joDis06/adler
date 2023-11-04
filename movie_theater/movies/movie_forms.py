from django import forms

class MovieForm(forms.Form):
   movie = forms.CharField(min_length=3, max_length=100, required=True)
   year = forms.IntegerField(min_value=1888, max_value=2025)
   actors = forms.CharField(min_length=3, max_length=1000, required=True)