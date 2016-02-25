from django.contrib.auth.models import User
from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=64)
    tiles = models.TextField()  # We'll put JSON in here
    character = models.ForeignKey('Character', related_name='levels')
    depth = models.PositiveSmallIntegerField(default=0)


class AbstractLocation(models.Model):
    current_level = models.ForeignKey('Level', related_name='+')
    x = models.PositiveSmallIntegerField()
    y = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True


class Character(AbstractLocation):
    """A character represents the player's avatar in game."""
    user = models.ForeignKey(User)
    name = models.CharField(max_length=16)

    # Hitpoints
    base_hp = models.PositiveIntegerField(default=500)
    current_hp = models.IntegerField(default=500)

    # Hunger
    max_food = models.PositiveIntegerField(default=30)
    current_food = models.IntegerField(default=30)


class CreatureType(models.Model):
    name = models.CharField(max_length=32)
    base_hp = models.PositiveIntegerField(default=500)


class Creature(AbstractLocation):
    creature = models.ForeignKey('CreatureType')
    current_hp = models.PositiveIntegerField()
