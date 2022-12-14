from django.shortcuts import render
from django.http import HttpResponse
from gestion.models import demande
from Agent.models import Personne
from gestion.forms import demandeForm


# Create your views here.

def tickete(request):
    return render(request,'ticket.html')

def FAQ(request):
    return render(request,'Faq.html')

def Lagent(request):
    return render(request, 'agent.html')

def personne_detail(request):
    personne=Personne.objects.all()
    return render(request,'agent.html',{'personne':personne})


def create_demande(request):
    if request.method=='POST':
        form=demandeForm(request.POST)
        if form.is_valid():
            Demande=form.save()
    else:
        form=demandeForm()  
    return render(request,'demande.html',{'form':form})


def demande_detail(request):
    Demande=demande.objects.all()
    return render(request,'ticket.html',{'Demande':Demande})

