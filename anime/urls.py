from django.urls import include, path
from rest_framework import routers
from .views import AnimeViewSet
from . import views

router = routers.DefaultRouter()
router.register('anime', AnimeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('<str:title>/',views.parace),
    path('api/<str:title>/', views.AnimeDetailView.as_view()),
    
]