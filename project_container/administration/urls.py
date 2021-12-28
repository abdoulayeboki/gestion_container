from django.urls import path
from .views import BienDetail, BienList, ClientDetail, ClientList, ContainerDetail, ContainerList, ConvoiDetail, ConvoiList, PaysList,PaysDetail,ArticleDetail,ArticleList, TypeBienDetail, TypeBienList

urlpatterns = [
    path('pays/', PaysList.as_view(), name='pays_list'),
    path('pays/<int:pk>', PaysDetail.as_view(), name='pays_detail'),
    path('clients', ClientList.as_view(), name='clients_list'),
    path('clients/<int:pk>', ClientDetail.as_view(), name='client_details'),
    path('articles/', ArticleList.as_view(), name='articles_list'),
    path('articles/<int:pk>', ArticleDetail.as_view(), name='articles_detail'),
    path('biens/', BienList.as_view(), name='biens_list'),
    path('biens/<int:pk>', BienDetail.as_view(), name='biens_detail'),
    path('type_biens/', TypeBienList.as_view(), name='typebiens_list'),
    path('type_biens/<int:pk>', TypeBienDetail.as_view(), name='typebiens_detail'),
    path('containers/', ContainerList.as_view(), name='containers_list'),
    path('containers/<int:pk>', ContainerDetail.as_view(), name='containers_detail'),
    path('convois/', ConvoiList.as_view(), name='convois_list'),
    path('convois/<int:pk>', ConvoiDetail.as_view(), name='convois_detail'),
]