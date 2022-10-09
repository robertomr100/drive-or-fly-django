from django import forms
from django.conf import settings


class TripForm(forms.Form):
    starting_destination = forms.CharField()
    final_destination = forms.CharField()
    date_start = forms.DateField(input_formats = settings.DATE_INPUT_FORMATS)
    date_end = forms.DateField(input_formats = settings.DATE_INPUT_FORMATS)