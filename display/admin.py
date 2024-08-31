# admin.py in your Django app

from django.contrib import admin
from .models import Game, Member, Unit, Viewer, Type

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'farm', 'owner', 'type_id', 'tag', 'tag_color', 'sex', 'sire', 'dam')
    search_fields = ('owner', 'tag', 'tag_color', 'sire', 'dam')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'is_admin')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit_id', 'sex', 'unit_cost', 'year', 'year_market_unit_value', 'year_market_value', 'year_value')
    search_fields = ('unit_id', 'unit_cost', 'year')

@admin.register(Viewer)
class ViewerAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_id', 'img')
    search_fields = ('id', 'type_id', 'img')

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('type_id', 'type_name', 'value')
    search_fields = ('type_name', 'value')
