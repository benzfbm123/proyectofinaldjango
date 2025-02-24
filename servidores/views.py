from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Servidor
from .forms import ServidorForm


@login_required
def lista_servidores(request):
    servidores = Servidor.objects.all()
    return render(request, 'servidores/lista_servidores.html', {'servidores': servidores})


def crear_servidor(request):
    if request.method == 'POST':
        form = ServidorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_servidores')
    else:
        form = ServidorForm()
    return render(request, 'servidores/crear_servidor.html', {'form': form})


def editar_servidor(request, pk):  
    servidor = get_object_or_404(Servidor, pk=pk)  
    if request.method == 'POST':
        form = ServidorForm(request.POST, instance=servidor)  
        if form.is_valid():
            form.save()  
            return redirect('lista_servidores') 
    else:
        form = ServidorForm(instance=servidor)  
    return render(request, 'servidores/editar_servidor.html', {'form': form})

def eliminar_servidor(request, pk):  
    servidor = get_object_or_404(Servidor, pk=pk) 
    if request.method == 'POST':
        servidor.delete()  
        return redirect('lista_servidores')  
    return render(request, 'servidores/eliminar_servidor.html', {'servidor': servidor})

def detalle_servidor(request, pk):
    servidor = get_object_or_404(Servidor, pk=pk)  
    return render(request, 'servidores/detalle_servidor.html', {'servidor': servidor})

@login_required
def lista_servidores(request):
    servidores = Servidor.objects.all()
    return render(request, 'servidores/lista_servidores.html', {'servidores': servidores})