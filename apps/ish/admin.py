from django.contrib import admin

from apps.ish.models import Client, Color, Saw, LaminateColor, Laminate, Edge, AddEdge, LaminatePrice


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "metr", "created_at")


@admin.register(Saw)
class SawAdmin(admin.ModelAdmin):
    list_display = ("name", "list_list", "created_at")


@admin.register(Edge)
class EdgeAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(Laminate)
class LaminateAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(LaminateColor)
class LaminateColorAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(AddEdge)
class AddEdgeAdmin(admin.ModelAdmin):
    list_display = ("name", "number")


@admin.register(LaminatePrice)
class LaminatePriceAdmin(admin.ModelAdmin):
    list_display = ('price',)
