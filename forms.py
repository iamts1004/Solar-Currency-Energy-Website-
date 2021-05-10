from django import forms
from . models import Energy_Table
from django.utils import timezone

class Sell(forms.ModelForm):    # to sell energy form.
    class Meta:
        model = Energy_Table
        fields = ['Name', 'Phone','Address','Energy','SolarEcoins']

class Buy(forms.ModelForm):    # to buy energy form.
    class Meta:
        model = Energy_Table
        fields = ['Name', 'Phone','Address','Energy','SolarEcoins']