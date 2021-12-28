from django.shortcuts import render
from .models import Client, Pays
from rest_framework import generics
from .serializer import ClientSerializer, PaysSerializer
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