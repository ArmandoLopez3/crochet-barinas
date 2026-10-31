from django.contrib import admin
from .models import Material, ProductoCrochet, DetalleMaterial

class DetalleMaterialInline(admin.TabularInline):
    model = DetalleMaterial
    extra = 1

@admin.register(ProductoCrochet)
class ProductoCrochetAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tejedor', 'horas_trabajo', 'fecha_creacion')
    inlines = [DetalleMaterialInline]

admin.site.register(Material)