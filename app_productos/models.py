from django.db import models

class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    fecha_añadido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
