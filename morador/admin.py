from django.contrib import admin
from . import models


class MoradorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email',
                    'situacao', 'cpf', 'data_nascimento', 'estado', 'situacao']


admin.site.register(models.Morador, MoradorAdmin)
