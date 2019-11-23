from django.shortcuts import render
from website.forms import PedidoForm

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
    return render(request, 'produtos.html')

def cadastro_pedido(request):
    form = PedidoForm(request.POST or None)
    print(form)
    if form.is_valid():
        form.save()
        print("if")
    context = {
        'formulario':form
    }

    return render(request, 'pedido.html', context)