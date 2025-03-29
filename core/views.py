from django.shortcuts import render, get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader
def index(request):
    print(request.user)
    produtos = Produto.objects.all()
    if str(request.user) == 'AnonymousUser': 
        teste = 'faça login no sistema'
    else:
        teste = 'autenticado!'
    context = {
        'nome': 'Name',
        'sobrenome': 'here',
        'logado': teste,
        'produtos': produtos
    }
    return render(request, 'index.html', context) 


def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    #prod = Produto.objects.get(pk=id)
    prod = get_object_or_404(Produto, pk=id)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html',context)


def error404(request,ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html', charset='utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html', charset='utf8', status=500)