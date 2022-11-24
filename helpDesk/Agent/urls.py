from django.urls import path #Fonction Path
from .import views

urlpatterns=[
    path('',views.Agent,name='Agent'),
    
    
    
     
]