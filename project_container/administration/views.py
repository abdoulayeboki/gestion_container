from django.shortcuts import render
from .models import Article, Bien, Client, Container, Convoi, Pays, TypeBien
from rest_framework import generics
from .serializer import ArticleSerializer, BienSerializer, ClientSerializer, ContainerSerializer, ConvoiSerializer, PaysSerializer, TypeBienSerializer
# Create your views here.

# view Pays   
class PaysList(generics.ListCreateAPIView):
    queryset = Pays.objects.all()
    serializer_class = PaysSerializer

    
class PaysDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pays.objects.all()
    serializer_class = PaysSerializer
    
# view Pays   
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    
class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
# view Article   
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# view Bien   
class BienList(generics.ListCreateAPIView):
    queryset = Bien.objects.all()
    serializer_class = BienSerializer

    
class BienDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bien.objects.all()
    serializer_class = BienSerializer

# view TypeBien   
class TypeBienList(generics.ListCreateAPIView):
    queryset = TypeBien.objects.all()
    serializer_class = TypeBienSerializer

    
class TypeBienDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeBien.objects.all()
    serializer_class = TypeBienSerializer

# view Convoi   
class ConvoiList(generics.ListCreateAPIView):
    queryset = Convoi.objects.all()
    serializer_class = ConvoiSerializer

    
class ConvoiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Convoi.objects.all()
    serializer_class = ConvoiSerializer
    
# view Container   
class ContainerList(generics.ListCreateAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer

    
class ContainerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer


