from django.shortcuts import render
from website.forms import PedidoForm
from website.models import *

# Create your views here.
def home(request):
    nome = 'Groger'
    idade = 18
    lista_roupas = [
        'Boné da lacoste',
        'Boné da Cycl0ne',
        'Cinto do Bátima',
        'Toca da Medusa',
        'Óculos Rift Zika'
    ]

    context = {
        'roupas': lista_roupas,
        'nome': nome,
        'idade': idade
    }
    
    return render(request, 'home.html', context)

def produtos(request):
    #lista_produtos = Produto.objects.all()
    lista_produtos = Produto.objects.filter(disponivel=True)
    context = {
        'produtos':lista_produtos
    } 
    return render(request, 'produtos.html', context)

def cadastro_pedido(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        context = {
            'msg': "Pedido realizado com sucesso"
        }
        return render(request, 'pedido.html', context)
    context = {
        'formulario':form
    }

    return render(request, 'pedido.html', context)