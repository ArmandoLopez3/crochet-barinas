from django.db import models
from django.conf import settings

class Material(models.Model):
    nombre = models.CharField(max_length=100)  # Ej: Hilo Pima, Lana, Relleno
    costo_unidad = models.DecimalField(max_digits=10, decimal_places=2)  # Costo por gramo o unidad
    unidad_medida = models.CharField(max_length=20, default='gramos')

    def __str__(self):
        return f"{self.nombre} (${self.costo_unidad}/{self.unidad_medida})"

class ProductoCrochet(models.Model):
    tejedor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'rol': 'TEJEDOR'},
        related_name='productos'
    )
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    horas_trabajo = models.DecimalField(max_digits=5, decimal_places=2, help_text="Horas invertidas en tejer")
    precio_hora = models.DecimalField(max_digits=10, decimal_places=2, help_text="Costo de la mano de obra por hora")
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def calcular_costo_total(self):
        costo_mano_obra = self.horas_trabajo * self.precio_hora
        costo_materiales = sum(detalle.costo_subtotal() for detalle in self.detalles_material.all())
        return costo_mano_obra + costo_materiales

    def __str__(self):
        return f"{self.nombre} - Tejido por: {self.tejedor.username}"

class DetalleMaterial(models.Model):
    producto = models.ForeignKey(ProductoCrochet, on_delete=models.CASCADE, related_name='detalles_material')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad_usada = models.DecimalField(max_digits=8, decimal_places=2)

    def costo_subtotal(self):
        return self.cantidad_usada * self.material.costo_unidad