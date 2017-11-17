from django.forms import ModelForm
from django import forms
from .models import Contact

class ContactForm(ModelForm):
    """コンタクトフォーム"""
    class Meta:
        model = Contact
        fields = ("name","mail","contact_text")

class GinSearchForm(forms.Form):
    """検索フォーム"""

    keyword = forms.CharField(label='キーワード', required=False)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['keyword'].widget.attrs['class'] = 'form-control'
        self.fields['keyword'].widget.attrs['placeholder'] = 'クイックサーチ'
