from django.shortcuts import render
from rest_framework import viewsets
from game.models import Character
from game.serializers import CharacterSerializer
# Create your views here.


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

