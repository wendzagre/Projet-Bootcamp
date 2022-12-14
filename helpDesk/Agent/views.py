from django.shortcuts import render
from django.http import HttpResponse
from Agent.models import Personne
from Agent.forms import PersonneForm


def create_agent(request):
    if request.method=='POST':
        form=PersonneForm(request.POST)
        if form.is_valid():
            personne=form.save() 
    else:
        form=PersonneForm()
    return render(request,'create_agent.html',{'form':form})



    

# Create your views here.
