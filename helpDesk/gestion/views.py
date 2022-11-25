from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Demande(request):
    return render(request,'demande.html')

def FAQ(request):
    return render(request,'Faq.html')

def Lagent(request):
    return render(request, 'create_agent.html')



def ticket(request):
    tickets=[
        {
            'Id':'1',
            'Matricule':'805pgt47',
            'Objet' :'Mise en place un réseau',
            'Description':'Problème Intégration à mon compte ALIAS',
            'Type':'Maintenance',
            'Ministère':"MENA",
            'Statut':'En Cours',
            'DateCréation':'12/4/2022',
            'HeureCréation':'10h15'
        },
        {
            'Id':'2',
            'Matricule':'805pgt70',
            'Objet' :'Mise en place un réseau',
            'Description':'Etat avancement salaire PRISCA',
            'Type':'RESEAU',
            'Ministère':"MEFP",
            'Statut':'Réglé',
            'DateCréation':'12/4/2022',
            'HeureCréation':'10h15'
        },
        {
            'Id':'3',
            'Matricule':'805pgt74',
            'Objet' :'Mise en place un réseau',
            'Description':'problème accès à mon compte SADIAN',
            'Type':'ALIAS',
            'Ministère':"MFPTPS",
            'Statut':'Clos',
            'DateCréation':'12/4/2022',
            'HeureCréation':'10h15'
        },
        {
            'Id':'4',
            'Matricule':'805pgt58',
            'Objet' :'Mise en place un réseau',
            'Description':'Problème accès à mon compte SIGASPE',
            'Type':'SADINA',
            'Ministère':"MSHPBE",
            'Statut':'Nouveau',
            'DateCréation':'12/4/2022',
            'HeureCréation':'10h15'
        },
    ]
    context={
          'tickets':tickets
        }
    return render(request,'ticket.html',context)


