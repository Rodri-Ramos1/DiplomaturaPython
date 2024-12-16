from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Cliente

"""def lista_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html',{'clientes':clientes})"""

def lista_cliente(request):
    clientes = Cliente.objects.all()
    clientes_data = [
        {   "id" : cliente.id,
            "nombre" : cliente.nombre,
            "apellido" : cliente.apellido,
            "cuit" : cliente.cuit,
            "email" : cliente.email,
            "telefono" : cliente.telefono,
        }
         for cliente in clientes
    ]
    return JsonResponse(clientes_data, safe = False)