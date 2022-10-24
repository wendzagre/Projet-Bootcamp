from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ticket(request):
    return render(request,'ticket.html')


