from django.urls import path

from . import views
from .views import CandidateDataAPI,CustomerSearchAPIView,CandidateDataIntAPI


urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
    path('a/parace/<str:name>/', views.parace, name='parace'),
    path('parace/<str:name>/', CandidateDataAPI.as_view(), name='parace-api'),
    path('prace/<str:name>/', views.prace_detail, name='prace_detail'),
    path('parace/int/<int:animeid>/', CandidateDataIntAPI.as_view(), name='candidate-data-int-api'),
    path('searchhhhh/', views.search_customers, name='search_customers'),
    path('api/customer/', CustomerSearchAPIView.as_view(), name='customer-search'),
]
