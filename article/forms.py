from django import forms
from django.forms import ModelForm
from .models import Page

class MySearchForm(forms.Form):
    keyword = forms.CharField(label='キーワード', required=False)

