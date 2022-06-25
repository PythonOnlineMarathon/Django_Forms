from django import forms
from author.models import Author


class AuthorForm(forms.ModelForm):

    
    class Meta:
        model = Author
        fields = ('name', 'patronymic','surname')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'patronymic': forms.TextInput(attrs={'class':'form-control'}),
            'surname': forms.TextInput(attrs={'class':'form-control'}),
        }
    