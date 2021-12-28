from rest_framework import serializers
from .models import Client, Pays
class PaysSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pays
        fields = ['code_pays', 'nom_pays']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['code_client', 'nom','prenom','adresse']