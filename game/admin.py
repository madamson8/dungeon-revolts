from django.contrib import admin

from game.models import Character, Level, CreatureType, Creature, ItemType, Item, \
    TileType


class CharacterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Character, CharacterAdmin)


class LevelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Level, LevelAdmin)


class CreatureTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(CreatureType, CreatureTypeAdmin)


class CreatureAdmin(admin.ModelAdmin):
    pass
admin.site.register(Creature, CreatureAdmin)


class ItemTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(ItemType, ItemTypeAdmin)


class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)


class TyleTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(TileType, TyleTypeAdmin)