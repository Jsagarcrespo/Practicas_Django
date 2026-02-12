from django.urls import path
#from tienda.views import compra

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("tienda/compra/", compra),
    path("tienda/saludo/", saludo),
    path("tienda/mensaje/", mensaje),
    path("prueba/compra/", pruebacompra),
]