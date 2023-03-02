from django.urls import path
from . import views

app_name = 'condominio'

urlpatterns = [
    path('', views.ListaCondomino.as_view(), name="lista")
]
