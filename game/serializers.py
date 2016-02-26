from rest_framework import serializers
from game.models import Character


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
