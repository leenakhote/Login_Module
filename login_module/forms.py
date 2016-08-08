
from django import forms

class Form(forms.Form):
    Username = forms.CharField(label='Your name', max_length=100)
