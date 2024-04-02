from django.urls import path

from .views import listar_users, create_regras, cadastrar_consumidores

urlpatterns = [
    path('', listar_users, name='index'),
    path('criar-regras/', create_regras, name='create_regras'),
    path('criar-consumidor/', cadastrar_consumidores, name='create_consumer'),
]
