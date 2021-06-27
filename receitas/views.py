from django.shortcuts import render
from .models import Receitas

# Create your views here.
def index(request):
    receitas = Receitas.objects.all()

    dados = {
        'nome_das_receitas': receitas
    }
    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')