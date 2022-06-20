
from django import forms

class familiaresformulario (forms.Form):

    nombre = forms.CharField()
    email = forms.EmailField()

class MenuesFormulario(forms.Form):   
    opciones= forms.CharField(max_length=30)
    email= forms.EmailField()
   


