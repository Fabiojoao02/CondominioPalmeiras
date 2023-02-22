from django.contrib import admin
from . import models


class BlocoInLine(admin.TabularInline):
    model = models.Bloco
    extra = 1


class CondominioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'Cidade', 'Estado', 'Bairro', 'Fracao_ideal_tem']
    inlines = [
        BlocoInLine
    ]


admin.site.register(models.Condominio, CondominioAdmin)
admin.site.register(models.Bloco)
