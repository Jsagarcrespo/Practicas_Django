from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
    productos = Producto.objects.all()
    return render(request, 'pedidos/listado.html', {'productos': productos})