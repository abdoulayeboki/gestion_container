from rest_framework import serializers
from .models import Article, Bien, Client, Convoi, Pays, TypeBien,Container
class PaysSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pays
        fields = ['code_pays', 'nom_pays']

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['code_client', 'nom','prenom','adresse']
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['code_article', 'nom_article']


class BienSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bien
        fields = ['code_bien', 'nom_bien','description']
class TypeBienSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeBien
        fields = ['code_typeBien', 'nom_typeBien','description']
class ContainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Container
        fields = ['code_container', 'nom_container','description']
class ConvoiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Convoi
        fields = ['code_convoi', 'date_depart','date_arrivee']