from rest_framework import serializers
from game.models import *


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
