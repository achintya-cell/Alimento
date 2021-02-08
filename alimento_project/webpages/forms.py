from django.forms import ModelForm
from .models import QuickOrder

class QuickOrderForm(ModelForm):
    class Meta:
        model = QuickOrder
        fields = ['city','name','email']