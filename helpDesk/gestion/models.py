from django.db import models
from random import choices

class demande(models.Model):    
    matricule=models.IntegerField()
    objet =models.fields.CharField(max_length=260)
    description=models.CharField(max_length=1000)
    Type=models.CharField(max_length=20)
    ministere=models.CharField(max_length=20)
    dateCreation=models.DateField()
    heureDemande=models.DateTimeField()
    statut=models.CharField(max_length=20)

  
    class Types(models.TextChoices):
        Maintenance = 'MAI'
        Reseau = 'RS'
        SIGASPE = 'SP'
        ALIAS = 'AS'
        SADINA = 'SA'
        PRISKA = 'PK'
        DIAN = 'DN'
        SITA = 'ST'
    Type=models.CharField(choices=Types.choices,max_length=5)

    class Ministere(models.TextChoices):
        MFPTPS = 'MF'
        MENA = 'MN'
        MUAFH = 'MU'
        MJDH = 'MJ'
        MAF = 'MA'
        MSHPB = 'MS'
        MEFP = 'ME'
        MTMUSRS='MTM'
        MATD='MD'
        MEA='EA'
        MCCAT='MCA'
        MESRI='MSI'
        MSAJ='JAS'
        MMC='CM'
        MEMC='MCE'
        MDICA='CAI'
    ministere=models.CharField(choices=Ministere.choices,max_length=5)

    class Statut(models.TextChoices):
        EnCours = 'EC'
        Regle = 'RE'
        Clos = 'CL'
        Nouveau = 'NV'
    statut=models.CharField(choices=Statut.choices,max_length=5)



  



