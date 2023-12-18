from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Categoria, Producto,CustomUser, Carrito, ItemCarrito,Pedido,DetallePedido,Marca

# Register your models here.
class CustomUserAdmin(UserAdmin):
    # Define cómo se mostrarán los campos en el admin
    list_display = ('username', 'email', 'nombre_completo', 'telefono_contacto', 'is_staff', 'is_active')
    # Otros atributos de configuración según tus necesidades

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(Pedido)
admin.site.register(DetallePedido)


