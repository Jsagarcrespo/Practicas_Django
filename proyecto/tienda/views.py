from django.shortcuts import render

# Create your views here.

def compra(request):
    return render(request, "tienda/compra.html")

def saludo(request):
    return render(request, "tienda/saludo.html")

def mensaje(request):
    leMensaje = "el mensaje se supone que viene desde la vista pyto"
    return render(request, "tienda/mensaje.html", {'mensaje': leMensaje})


