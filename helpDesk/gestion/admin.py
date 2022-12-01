from django.contrib import admin

from gestion.models import demande

class DemandeAdmin(admin.ModelAdmin):
    list_display=('matricule','objet','description','Type','ministere','dateCreation','heureDemande','statut')

admin.site.register(demande,DemandeAdmin)

# Register your models here.
