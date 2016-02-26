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


class CreatureTypeViewSet(viewsets.ModelViewSet):
    queryset = CreatureType.objects.all()
    serializer_class = CreatureTypeSerializer


class CreatureViewSet(viewsets.ModelViewSet):
    queryset = Creature.objects.all()
    serializer_class = CreatureSerializer


class ItemTypeViewSet(viewsets.ModelViewSet):
    queryset = ItemType.objects.all()
    serializer_class = ItemTypeSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class TileTypeViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = TileTypeSerializer
