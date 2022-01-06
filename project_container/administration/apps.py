from django.apps import AppConfig
# from suit.apps import DjangoSuitConfig

class AdministrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'administration'

# class DjangoSuit(DjangoSuitConfig):
#     layout = 'vertical'