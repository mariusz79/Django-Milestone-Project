from django import forms


class ContactForm(forms.Form):
    """simple contact form"""
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)