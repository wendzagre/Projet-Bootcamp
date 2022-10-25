from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ticket(request):
    tickets=[
        {
            'Id':'1',
            'Objet' :'Mise en place un réseau',
            'Description':'SIGASPE',
            'Type':'RESEAU',
            'Statut':'Réglé',
            'DateCréation':'12/4/2022',
            'HeureCréation':'10h15'
        },
        {
            'Id':'1',
            'Objet' :'Mise en place un réseau',
            'Description':'SIGASPE',
            'Type':'RESEAU',
            'Statut':'Réglé',
            'DateCréation':'12/4/2022',
            'HeureCréation':'10h15'
        },
        {
            'Id':'1',
            'Objet' :'Mise en place un réseau',
            'Description':'SIGASPE',
            'Type':'RESEAU',
            'Statut':'Réglé',
            'DateCréation':'12/4/2022',
            'HeureCréation':'10h15'
        },
        {
            'Id':'1',
            'Objet' :'Mise en place un réseau',
            'Description':'SIGASPE',
            'Type':'RESEAU',
            'Statut':'Réglé',
            'DateCréation':'12/4/2022',
            'HeureCréation':'10h15'
        },
    ]
    context={
          'tickets':tickets
        }
    return render(request,'ticket.html',context)


