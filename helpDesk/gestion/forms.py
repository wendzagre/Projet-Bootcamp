from django import forms
from gestion.models import demande

class demandeForm(forms.ModelForm):
    class Meta:
        model=demande
        fields='__all__'

        widgets={
            'matricule':forms.NumberInput(attrs={'class':'form-control '}),
            'objet':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control '}),
            'Type':forms.Select(attrs={'class':'form-control'}),
            'ministere':forms.Select(attrs={'class':'form-control'}),
            'dateCreation':forms.DateInput(attrs={'class':'form-control'}),
            'heureDemande':forms.DateTimeInput(attrs={'class':'form-control'}),
            'statut':forms.Select(attrs={'class':'form-control'}),

        }