from django.contrib import admin

from game.models import Character


class CharacterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Character, CharacterAdmin)
