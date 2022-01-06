from django.contrib import admin

from .models import Bien, Client, Container, Convoi, Pays,Article, TypeBien

admin.site.site_header ="Clic magic administration"
# Register your models here.
class PaysAdmin(admin.ModelAdmin):
    list_display   = ('code_pays', 'nom_pays')
    search_fields  = ('code_pays', 'nom_pays')
    
admin.site.register(Pays, PaysAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display   = ('code_article', 'nom_article','description')
    list_filter    = ('client',)
    search_fields  = ('code_article', 'nom_article')
class BienAdmin(admin.ModelAdmin):
    list_display   = ('code_bien', 'nom_bien','description')
    list_filter    = ('typeBien',)
    search_fields  = ('code_bien', 'nom_bien')

class TypeBienAdmin(admin.ModelAdmin):
    list_display   = ('code_typeBien', 'nom_typeBien','description')
    search_fields  = ('code_typeBien', 'nom_typeBien')

class ContainerAdmin(admin.ModelAdmin):
    list_display   = ('code_container', 'nom_container','description')
    list_filter    = ('convoi',)
    search_fields  = ('code_container', 'nom_container')
class ClientAdmin(admin.ModelAdmin):
    list_display   = ('code_client', 'nom','prenom','adresse','email','telephon')
    list_filter    = ('pays',)
    search_fields  = ('code_client', 'nom','prenom')

class ConvoiAdmin(admin.ModelAdmin):
    list_display   = ('code_convoi', 'date_depart','date_arrivee','pays_actuel','pays_arrive','pays_depart')
    search_fields  = ('code_convoi',)
    list_filter    = ( 'date_depart','pays_actuel','pays_arrive','pays_depart')
admin.site.register(Article, ArticleAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Bien,BienAdmin)
admin.site.register(TypeBien,TypeBienAdmin)
admin.site.register(Container,ContainerAdmin)
admin.site.register(Convoi,ConvoiAdmin)