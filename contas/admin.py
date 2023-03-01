from django.contrib import admin
from . import models

<<<<<<< HEAD
admin.site.register(models.Contas)
=======

class ContasAdmin(admin.ModelAdmin):
    list_display = ['nome', 'situacao']


admin.site.register(models.Contas, ContasAdmin)
>>>>>>> master
