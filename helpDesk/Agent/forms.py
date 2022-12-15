from django import forms
from Agent.models import Personne

class PersonneForm(forms.ModelForm):
    class Meta:
        model=Personne
        fields='__all__'

        widgets={
            'nom':forms.TextInput(attrs={'class':'form-control '}),
            'prenom':forms.TextInput(attrs={'class':'form-control'}),
            'telephone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'actif':forms.NullBooleanSelect(attrs={'class':'form-control'}),
            'dateCreation':forms.DateInput(attrs={'class':'form-control'}),

        }

