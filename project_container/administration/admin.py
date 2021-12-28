from django.contrib import admin

from .models import Bien, Client, Container, Convoi, Pays,Article, TypeBien

# Register your models here.
class PaysAdmin(admin.ModelAdmin):
    list_display   = ('code_pays', 'nom_pays')
    # search_fields  = ('code', 'nom')
admin.site.register(Pays, PaysAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display   = ('code_article', 'nom_article')
    # search_fields  = ('code', 'nom')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Client)
admin.site.register(Bien)
admin.site.register(TypeBien)
admin.site.register(Container)
admin.site.register(Convoi)