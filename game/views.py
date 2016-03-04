from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from game import models as m
from game import serializers as s
from game.game import draw_board, execute_move


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = m.Character.objects.all()
    serializer_class = s.CharacterSerializer

    @detail_route(methods=["POST"])
    def move(self, request, pk=None):
        # Take in a string command
        command = request.data.get('command')
        if not command:
            raise ValidationError("You must supply a command.")

        # Get some data
        character = self.get_object()

        # Execute the move
        execute_move(character, command)

        # Return the new board state, and any messages
        data = draw_board(character)

        return Response(data, status=200)


class LevelViewSet(viewsets.ModelViewSet):
    queryset = m.Level.objects.all()
    serializer_class = s.LevelSerializer


class CreatureTypeViewSet(viewsets.ModelViewSet):
    queryset = m.CreatureType.objects.all()
    serializer_class = s.CreatureTypeSerializer


class CreatureViewSet(viewsets.ModelViewSet):
    queryset = m.Creature.objects.all()
    serializer_class = s.CreatureSerializer


class ItemTypeViewSet(viewsets.ModelViewSet):
    queryset = m.ItemType.objects.all()
    serializer_class = s.ItemTypeSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = m.Item.objects.all()
    serializer_class = s.ItemSerializer


class TileTypeViewSet(viewsets.ModelViewSet):
    queryset = m.TileType.objects.all()
    serializer_class = s.TileTypeSerializer
