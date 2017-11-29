from django import forms
from django.forms import ModelForm
from .models import Page

class MySearchForm(forms.Form):
    keyword = forms.CharField(label='', required=False)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['keyword'].widget.attrs['class'] = 'form-control'
        self.fields['keyword'].widget.attrs['placeholder'] = 'クイックサーチ'