from django.shortcuts import render
from .serializers import SingerSerializer,SongSerializer
from .models import Song,Singer
from rest_framework import viewsets

class SingerViewset(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongViewset(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer