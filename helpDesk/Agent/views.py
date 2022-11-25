from django.shortcuts import render
from django.http import HttpResponse



def Agent(request):
    compte=[
        {
        'id':'1',
        'nom':'ZAGRE',
        'prenom':'Patrick',
        'telephone':'72947683',
        'email':'patrickzagre3@gmail.com',
        'actif':'True',
        'dateCreation':'26-10-2022'
        },

        {
        'id':'1',
        'nom':'ZAGRE',
        'prenom':'Patrick',
        'telephone':'72947683',
        'email':'patrickzagre3@gmail.com',
        'actif':'True',
        'dateCreation':'26-10-2022'

        },

        {
        'id':'1',
        'nom':'ZAGRE',
        'prenom':'Patrick',
        'telephone':'72947683',
        'email':'patrickzagre3@gmail.com',
        'actif':'True',
        'dateCreation':'26-10-2022'
        },
    ]
    context={
          'compte':compte
        }
    return render(request,'agent.html',context)
    

# Create your views here.
