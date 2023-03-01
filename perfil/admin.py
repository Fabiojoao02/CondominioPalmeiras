from django.contrib import admin
from . import models

<<<<<<< HEAD
admin.site.register(models.Perfil)
=======

class PerfilAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'situacao']


admin.site.register(models.Perfil, PerfilAdmin)
>>>>>>> master
