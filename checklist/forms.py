from django import forms

class ItemForm(forms.Form):
    description = forms.CharField(label='Your name', max_length=300)