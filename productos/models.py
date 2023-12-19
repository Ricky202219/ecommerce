from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nombre_completo = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    direccion_envio = models.CharField(max_length=200)
    telefono_contacto = models.CharField(max_length=20)
    region = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set')

    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_set')
    
class Categoria(models.Model):
    imagen = models.CharField(max_length=200)
    nombre = models.CharField(max_length=100)
    # Otros campos que necesites
    
    def __str__(self):
        return self.nombre

class Marca(models.Model):
    imagen = models.CharField(max_length=200)
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # Otros campos que necesites
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    imagen = models.CharField(max_length=200)
    nombre = models.CharField(max_length=100)
    categoria = models.ManyToManyField(Categoria)
    marca=models.ManyToManyField(Marca)
    precio = models.IntegerField()
    stock = models.IntegerField()
    
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.nombre    

class Carrito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='ItemCarrito')
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

    def total_carrito(self):
        total = 0
        items_carrito = self.itemcarrito_set.all()
        for item in items_carrito:
            total += item.subtotal()
        return total

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad

class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)
    # Puedes agregar más campos según tus necesidades

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    # Puedes agregar más campos según tus necesidades

