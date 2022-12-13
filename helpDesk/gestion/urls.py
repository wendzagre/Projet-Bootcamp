from django.urls import path #Fonction Path
from .import views #raccourci pour le repertoire courant

#URL patterns pour chaque ligne
urlpatterns=[
    path('',views.ticket,name='ticket'),
    

]

# '': chaine vide et /
# views.ticket : fonction ticket dans views.py
# name ='ticket' : nom de la route