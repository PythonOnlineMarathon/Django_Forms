from django import forms
from author.models import Author
from book.models import Book


class BookFilterForm(forms.Form):

    name = forms.CharField(label='Title',required=False)
    min_count = forms.IntegerField (label='Count from',required=False)
    max_count = forms.IntegerField (label='Count to  ',required=False)
    authors = [(author.id, author.name +' '+ author.patronymic +' '+ author.surname) for author in Author.objects.all()]
    author = forms.MultipleChoiceField(label='Author', widget=forms.CheckboxSelectMultiple,
            choices=authors, required=False)
    
class BookForm(forms.ModelForm):

    
    class Meta:
        model = Book
        fields = ('name', 'description','count','authors')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'count': forms.TextInput(attrs={'class':'form-control'}),
            'authors': forms.SelectMultiple(attrs={'class':'form-control'}),    
        }
