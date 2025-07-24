from django import forms

class JsloadForm(forms.Form):
    file = forms.FileField()