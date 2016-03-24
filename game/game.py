import random

from rest_framework.exceptions import ValidationError

from game.models import Character, Level, Creature, CreatureType


def draw_board(character: Character):
    # If the character is dead,
    if character.current_hp <= 0:
        raise ValidationError("Cannot generate level. Character is dead")
    level = character.current_level
    if not level:
        level = generate_level(character)
    width = level.width
    tiles = [c for c in level.tiles.strip("\n")]

    def set_character(x, y, char):
        position = x + y * (width + 1)
        tiles[position] = char

    # Where is the character on this level?
    set_character(character.x, character.y, "@")

    # For each creature in the level, set it.
    for creature in Creature.objects.filter(current_level=level):
        creature.move(character)
        set_character(creature.x, creature.y, creature.type.symbol)
    return "".join(tiles)


def generate_level(character: Character):
    # Build the tiles
    level = Level(
        name="The Beginning",
        depth=1,
        tiles="""
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
""",
        character=character,
    )
    level.save()

    # Add the character to this level
    character.current_level = level
    character.x = 5
    character.y = 5
    character.save()

    # Create a creature
    ctype = random.choice([c for c in CreatureType.objects.all()])
    c = Creature(
        current_level=level,
        x=0, y=0,
        type=ctype,
        current_hp=ctype.base_hp
    )
    c.save()

    return level


def execute_move(character, command):
    # If the character is dead, don't accept commands
    if character.current_hp <= 0:
        raise ValidationError("You are dead!")
    if not character.current_level:
        generate_level(character)

    command = command.split(" ")
    if command[0] == "move":
        direction_string = command[1]
        direction = {
            "east": (1, 0),
            "west": (-1, 0),
            "north": (0, -1),
            "south": (0, 1),
        }[direction_string]

    # if command[0] == "attack":
    #     attack_string = command[1]
    #     attack_string = {
    #         "east": (1, 0),
    #         "west": (-1, 0),
    #         "north": (0, -1),
    #         "south": (0, 1),
    #     }

        # Update the character position
        character.x += direction[0]
        character.y += direction[1]
        # If the character is out of bounds, kill it
        w = character.current_level.width
        h = character.current_level.height
        print(character.x, character.y, w, h)
        if (character.x < 0 or
            character.y < 0 or
            character.x >= w or
            character.y >= h):
            character.current_hp = -1

        character.save()
    else:
        raise ValidationError("Illegal Move")
