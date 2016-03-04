from django.contrib.auth.models import User
from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=64)
    tiles = models.TextField()  # We'll put JSON in here
    character = models.ForeignKey('Character', related_name='levels')
    depth = models.PositiveSmallIntegerField(default=0)

    @property
    def width(self):
        return len(self.tiles.strip("\n").split("\n")[0])

    @property
    def height(self):
        return len(self.tiles.strip("\n").split("\n"))

    def __str__(self):
        return "{}: {} ({})".format(self.depth, self.name, self.depth)


class AbstractLocation(models.Model):
    current_level = models.ForeignKey(
        'Level', related_name='+', blank=True, null=True, on_delete=models.SET_NULL)
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

    # Sin count
    sin_level = models.SmallIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.user)


class CreatureType(models.Model):
    name = models.CharField(max_length=32)
    base_hp = models.PositiveIntegerField(default=500)
    enemy_damage = models.SmallIntegerField(default=0)
    enemy_aggro = models.BooleanField(default=True)
    symbol = models.CharField(max_length=1)

    def __str__(self):
        return "{} ({})".format(self.name, self.symbol)


class Creature(AbstractLocation):
    type = models.ForeignKey('CreatureType')
    current_hp = models.PositiveIntegerField()

    def __str__(self):
        char_name = ""
        if self.current_level:
            char_name = self.current_level.character
        return "{} ({})".format(self.type, char_name)


class ItemType(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(default='description')
    health = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    durability = models.IntegerField(default=30)
    consumable = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.name)


class Item(AbstractLocation):
    type = models.ForeignKey('ItemType')
    current_durability = models.PositiveIntegerField()


class TileType(models.Model):
    name = models.CharField(max_length=16)
    damage = models.IntegerField(default=0)
    is_solid = models.BooleanField(default=True)
    floor = models.BooleanField(default=True)

    def __str__(self):
        char_name = ""
        if self.current_level:
            char_name = self.current_level.character
        return "{} {}".format(self.type, char_name)

