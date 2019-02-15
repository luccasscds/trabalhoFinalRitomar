from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import EstoqueForm



def index(request):
    return render(request, 'index.html')

def estoque_list(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque_list.html', {'produtos': produtos})

def estoque_cadastro(request):
    formulario = EstoqueForm(request.POST, None)

    if formulario.is_valid():
        formulario.save()
        return redirect('estoque_list')
    return render(request, 'estoque_form.html', {'formulario':formulario})

def estoque_atualizar(request, id):
    produto = get_object_or_404(Produto, pk=id)
    formulario = EstoqueForm(request.POST or None, instance=produto)

    if formulario.is_valid():
        formulario.save()
        return redirect('estoque_list')

    return render(request, 'estoque_form.html', {'formulario': formulario})

def estoque_deletar(request, id):
    produto = get_object_or_404(Produto, pk=id)
    formulario = EstoqueForm(request.POST or None, instance=produto)

    if request.method == 'POST':
        produto.delete()
        return redirect('estoque_list')

    return render(request, 'estoque_confirm_delecao.html', {'produto': produto})




