from django.db import models



class Personne(models.Model):
    nom=models.CharField(max_length=10)
    prenom=models.CharField(max_length=40)
    telephone=models.IntegerField()
    email=models.EmailField()
    actif=models.BooleanField(default=False)
    dateCreation=models.fields.DateField()


    

