<<<<<<< HEAD
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.db import models
=======
from django.db import models
from django.contrib.auth.models import User
>>>>>>> master


class Perfil(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    situacao = models.CharField(
        max_length=1, default='A', verbose_name='Situação')

    def __str__(self):
<<<<<<< HEAD
        return f'{self.usuario.first_name} {self.usuario.last_name}'
=======
        # return f'{self.usuario.first_name} {self.usuario.last_name}'
        return f'{self.usuario.first_name}'
>>>>>>> master

    def clean(self):
        pass

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
