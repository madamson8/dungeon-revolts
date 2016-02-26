from rest_framework import serializers
from game.models import *


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level


class CreatureTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatureType


class CreatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creature


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item


class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType


class TileTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TileType
