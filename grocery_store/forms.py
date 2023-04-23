from django import forms
from .models import *

class RiceForm(forms.ModelForm):
    class Meta:
        model = Rice
        fields = ('type', 'price', 'status', 'offers')


class BakeryForm(forms.ModelForm):
    class Meta:
        model = Bakery
        fields = ('type', 'price', 'status', 'offers')
        

class DairyForm(forms.ModelForm):
    class Meta:
        model = Dairy_products
        fields = ('type', 'price', 'status', 'offers')

class DrinksForm(forms.ModelForm):
    class Meta:
        model = Drinks
        fields = ('type', 'price', 'status', 'offers')

class SpicesForm(forms.ModelForm):
    class Meta:
        model = Spices
        fields = ('type', 'price', 'status', 'offers')