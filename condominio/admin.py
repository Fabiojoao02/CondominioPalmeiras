from django.contrib import admin
from . import models


class BlocoInLine(admin.TabularInline):
    model = models.Bloco
    extra = 1


class CondominioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'Cidade', 'Estado',
                    'Bairro', 'Fracao_ideal_tem']
    inlines = [
        BlocoInLine
    ]


<<<<<<< HEAD
class Bloco_MoradorInLine(admin.TabularInline):
    model = models.Bloco_Morador
    extra = 1


class BlocoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    inlines = [
        Bloco_MoradorInLine
    ]


class Bloco_MoradorAdmin(admin.ModelAdmin):
    def nome_bloco(self, obj):
        return obj.bloco.nome

    list_display = ['nome', 'cpf', 'telefone',
                    'email', 'estado', 'nome_bloco']


admin.site.register(models.Condominio, CondominioAdmin)
admin.site.register(models.Bloco, BlocoAdmin)
admin.site.register(models.Bloco_Morador, Bloco_MoradorAdmin)
=======
admin.site.register(models.Condominio, CondominioAdmin)
admin.site.register(models.Bloco)
>>>>>>> master
