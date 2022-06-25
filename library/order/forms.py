from django import forms
from .models import Order


class OrderForm(forms.ModelForm, forms.Form):
    class Meta:
        model = Order
        fields = ('user', 'book')        

   
