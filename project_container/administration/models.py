from django.db import models

# Create your models here.
from django.db import models

# Register your models here.
class Pays(models.Model):
    code_pays = models.CharField(max_length=25,unique=True)
    nom_pays = models.CharField(max_length=100, unique=True)
    
    def __str__(self) :
        return self.nom_pays
class Container(models.Model):
    code_container = models.CharField(max_length=25,unique=True)
    nom_container = models.CharField(max_length=100)
    description = models.TextField()
class Client(models.Model):
    code_client = models.CharField(max_length=25,unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    telephon = models.CharField(max_length=18,default=None)
    email = models.CharField(max_length=100)
    code_postal=models.IntegerField()
    pays = models.ForeignKey(Pays, related_name="clients",null=True,on_delete=models.SET_NULL)
    
    def __str__(self) :
        return self.nom
class Article(models.Model):
    code_article = models.CharField(max_length=25,unique=True)
    nom_article = models.CharField(max_length=100)
    description = models.TextField()
    client= models.ForeignKey(Client, related_name="articles", null=True,on_delete=models.SET_NULL)
    container= models.ForeignKey(Container, related_name="articles", null=True,on_delete=models.SET_NULL)
class TypeBien(models.Model):
    code_typeBien = models.CharField(max_length=25,unique=True)
    nom_typeBien = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.nom_typeBien
class Bien(models.Model):
    code_bien = models.CharField(max_length=25,unique=True)
    nom_bien = models.CharField(max_length=100)
    description = models.TextField()
    article= models.ForeignKey(Article, related_name="biens", null=True,on_delete=models.SET_NULL)
    typeBien= models.ForeignKey(TypeBien, related_name="biens", null=True,on_delete=models.SET_NULL)



class Convoi(models.Model):
    code_convoi = models.CharField(max_length=25,unique=True)
    date_depart = models.DateTimeField()
    date_arrivee = models.DateTimeField()
    description = models.TextField()
    containers = models.ManyToManyField(Container)
    pays_depart = models.ForeignKey(Pays, null=True,on_delete=models.SET_NULL)
    pays_arrive = models.ForeignKey(Pays,related_name="arrive", null=True,on_delete=models.SET_NULL)
    pays_actuel = models.ForeignKey(Pays,related_name="acuel",null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.code_convoi