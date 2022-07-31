
from django import forms
from .models import BlogModel, CardModel
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class BlogForms(forms.ModelForm):
    telephone = PhoneNumberField(
        widget = PhoneNumberPrefixWidget(initial='TG'),
        required = False, 
    )
    
    class Meta:
        model = BlogModel
        fields = ("nom", "prenom", "email", "telephone")

class CardForms(forms.ModelForm):    
    class Meta:
        model = CardModel
        fields = ("title", "description", "image")