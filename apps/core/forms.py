from django import forms
from core.models import Person, Phone

class PersonForm(forms.Form):
    class Meta:
        help_texts = {
            'name': 'Digite o nome do usuario'
        }


    name = forms.CharField(max_length=255, min_length=10, label='Nome', help_text='Texto Ajuda')
    email = forms.EmailField(max_length=254, label='Email')
    is_active = forms.BooleanField(required=False, label='Ativo', initial=False)
    phone = forms.ModelMultipleChoiceField(label='Telefone', queryset=Phone.objects.all())
