from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='email')
    tel = forms.CharField(label='tel')
    message = forms.CharField(label='message', max_length=512)
