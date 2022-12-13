from django.urls import path #Fonction Path
from .import views

urlpatterns=[
    path('',views.create_agent,name='Agent'),

    
    
     
]