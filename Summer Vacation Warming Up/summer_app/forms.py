from django import forms

class photoForm(forms.Form):
    subject = forms.CharField(max_length=200)
    content = forms.CharField()
    photo = forms.ImageField()
    create_date = forms.DateField()