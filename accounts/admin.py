from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class CustomUserAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('rol', 'telefono', 'ubicacion')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Adicional', {'fields': ('rol', 'telefono', 'ubicacion')}),
    )
    list_display = ['username', 'email', 'rol', 'is_staff']

admin.site.register(Usuario, CustomUserAdmin)