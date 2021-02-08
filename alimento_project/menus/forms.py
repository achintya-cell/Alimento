from django import forms
from .models import Menu,Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['items',]