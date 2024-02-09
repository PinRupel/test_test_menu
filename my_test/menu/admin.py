from django.contrib import admin

from menu.models import MainMenu, Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fields = ['title']


@admin.register(MainMenu)
class MainMenuAdmin(admin.ModelAdmin):
    fields = ['menu', 'name', 'slug', 'parent']
