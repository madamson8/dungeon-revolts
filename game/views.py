from django.shortcuts import render
from rest_framework import viewsets
from game.models import *
from game.serializers import *
# Create your views here.


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
