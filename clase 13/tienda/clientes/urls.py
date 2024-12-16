from django.urls import path

from . import views

urlpatterns = [ 
    path('clientes/', views.lista_cliente, name = 'lista_cliente')
]
   
