from django.shortcuts import render

# Create your views here.
#Vista de la página de login
def index(request):
 return render(request, 'pago/index.html')