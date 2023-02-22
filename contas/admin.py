from django.contrib import admin
from . import models


class ContasAdmin(admin.ModelAdmin):
    list_display = ['nome', 'situacao']


admin.site.register(models.Contas, ContasAdmin)
