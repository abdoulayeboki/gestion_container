from django.urls import path
from .views import ClientDetail, ClientList, PaysList,PaysDetail

urlpatterns = [
    path('pays', PaysList.as_view(), name='pays_list'),
    path('pays/<int:pk>', PaysDetail.as_view(), name='pays_detail'),
    path('clients', ClientList.as_view(), name='clients_list'),
    path('clients/<int:pk>', ClientDetail.as_view(), name='clients_detail'),
]