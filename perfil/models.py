from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    situacao = models.CharField(
        max_length=1, default='A', verbose_name='Situação')

    def __str__(self):
        # return f'{self.usuario.first_name} {self.usuario.last_name}'
        return f'{self.usuario.first_name}'

    def clean(self):
        pass

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
