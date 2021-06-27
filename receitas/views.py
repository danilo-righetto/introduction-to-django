from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receitas

# Create your views here.
def index(request):
    receitas = Receitas.objects.all()

    dados = {
        'nome_das_receitas': receitas
    }
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)
    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receita.html', receita_a_exibir)