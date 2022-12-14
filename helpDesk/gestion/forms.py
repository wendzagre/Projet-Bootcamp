from django import forms
from gestion.models import demande

class demandeForm(forms.ModelForm):
    class Meta:
        model=demande
        fields='__all__'