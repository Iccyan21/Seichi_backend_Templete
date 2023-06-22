from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Anime
from .serializers import AnimeSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

class AnimeViewSet(viewsets.ModelViewSet):
   queryset = Anime.objects.all()
   serializer_class = AnimeSerializer



def parace(request,title):   
    Candidate_data = get_object_or_404(Anime, title=title)
    params = {
        'Candidate_data': Candidate_data,
    }
    return render(request,'anime/index.html',params)


 
class AnimeDetailView(APIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Anime.objects.all()

    def get(self, request, title):
        anime = get_object_or_404(Anime, title=title)
        serializer = AnimeSerializer(anime)
        return Response(serializer.data)