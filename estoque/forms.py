from django.forms import ModelForm
from .models import Produto


class EstoqueForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'qtd_estoque', 'descricao']

