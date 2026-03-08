from django.db import models
from usuario.models import Usuario 
from producto.models import Producto

# Create your models here.

class Pedido(models.Model):

    ESTADOS = [
        ("PENDIENTE", "Pendiente"),
        ("PAGADO", "Pagado"),
        ("CANCELADO", "Cancelado"),
    ]

    usuario = models.ForeignKey(Usuario, on_delete= models.PROTECT)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="PENDIENTE")
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id - {self.estado}}" 



class LineaPedido(models.Model):

    pedido = models.ForeignKey("Pedido", on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto}"

