from django.shortcuts import render, redirect, get_object_or_404
from .forms import VeiculoForm
from django.contrib import messages
from .models import Veiculo


# Create your views here.
def home(request):

    veiculos = Veiculo.objects.all()
    return render(request, 'index.html', {'veiculos': veiculos} )


def form_view(request):
    if request.method == 'POST':
         form = VeiculoForm(request.POST)
         form.save()
         messages.success(request, "Veículo cadastrado com sucesso")
         return redirect('form_view')

    else:
        form = VeiculoForm()

    return render(request, 'uni_form.html', {'form': form})


def edit(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    form = VeiculoForm(instance=veiculo)
    return render(request, 'uni_form.html', {'form': form, 'veiculo': veiculo})



def delete(request, id):
    veiculo  = get_object_or_404(Veiculo, id=id)
    veiculo.delete()
    messages.success(request, 'Veículo deletado com sucesso')
    return redirect('home')



