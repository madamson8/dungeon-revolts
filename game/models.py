from django.contrib.auth.models import User
from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=64)
    tiles = models.TextField()  # We'll put JSON in here
    character = models.ForeignKey('Character', related_name='levels')
    depth = models.PositiveSmallIntegerField(default=0)


class AbstractLocation(models.Model):
    current_level = models.ForeignKey(
        'Level', related_name='+', blank=True, null=True)
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
    enemy_damage = models.SmallIntegerField(default=0)
    enemy_aggro = models.BooleanField(default=True)


class Creature(AbstractLocation):
    type = models.ForeignKey('CreatureType')
    current_hp = models.PositiveIntegerField()


class ItemType(models.Model):
    name = models.CharField(max_length=32)
    health = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    durability = models.IntegerField(default=30)
    consumable = models.BooleanField(default=False)


class Item(AbstractLocation):
    type = models.ForeignKey('ItemType')
    current_durability = models.PositiveIntegerField()