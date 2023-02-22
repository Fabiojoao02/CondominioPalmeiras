from django.contrib import admin
from . import models


class PerfilAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'situacao']


admin.site.register(models.Perfil, PerfilAdmin)
