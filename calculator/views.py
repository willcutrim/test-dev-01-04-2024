from django.shortcuts import render, redirect
from calculator_python import calculator
from calculator.models import RegrasDeDesconto, Consumer

from .forms import ConsumerForm, RegrasDeDescontoForm
def listar_users(request):

    return render(request, 'calculator/list.html', {'regras': Consumer.objects.all()})
    


def cadastrar_consumidores(request):
    if request.method == 'POST':
        form = ConsumerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ConsumerForm()
    context = {
        'form': form
    }
    return render(request, 'calculator/create_consumer.html', context)



def create_regras(request):
    if request.method == 'POST':
        form = RegrasDeDescontoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_regras')
    else:
        form = RegrasDeDescontoForm()
    context = {
        'form': form
    }
    return render(request, 'calculator/create_regras.html', context)
