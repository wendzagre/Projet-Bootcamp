from django.contrib import admin

from Agent.models import Personne


class PersonneAdmin(admin.ModelAdmin):
    list_display=('nom','prenom','telephone','email','actif','dateCreation')

admin.site.register(Personne,PersonneAdmin)




# Register your models here.
