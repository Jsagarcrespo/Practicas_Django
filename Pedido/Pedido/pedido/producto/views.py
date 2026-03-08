from django.shortcuts import render
from .models import Producto
# Create your views here.
#Vista de la página de login
def index(request):
 productos = Producto.objects.all()
 return render(request, 'producto/index.html', {'productos': productos})