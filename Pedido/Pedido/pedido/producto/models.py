from django.db import models

# Create your models here.

class Producto(models.Model):

    nomProduct = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nomProduct