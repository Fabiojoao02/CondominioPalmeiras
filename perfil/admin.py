from django.contrib import admin
from . import models


class PerfilInLine(admin.TabularInline):
    model = models.Perfil
    extra = 1


class PerfilAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'situacao']
    inlines = [
        PerfilInLine
    ]


admin.site.register(models.Perfil)
