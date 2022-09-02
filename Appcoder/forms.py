from django import forms

class renault1(forms.Form):
    modelo=forms.CharField(max_length=50)
    velocidad=forms.IntegerField()
    caballos_fuerza=forms.IntegerField()
    

