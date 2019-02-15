from django.urls import path
from .views import index
from .views import estoque_list
from .views import estoque_cadastro
from .views import estoque_atualizar
from .views import estoque_deletar

urlpatterns = [
    path('', index, name='index'),
    path('lista/', estoque_list, name='estoque_list'),
    path('cadastro/', estoque_cadastro, name='estoque_cadastro'),
    path('atualizar/<int:id>/', estoque_atualizar, name='estoque_atualizar'),
    path('deletar/<int:id>/', estoque_deletar, name='estoque_deletar'),

]