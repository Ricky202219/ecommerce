"""projectofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from productos import views as vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vistas.renderIndex, name='home'),
    #path('productos/',vistas.renderProductos),
    #path('producto/',vistas.renderProducto),
    path('terminos/',vistas.renderTerminos),
    path('preguntas/',vistas.renderPreguntas),
    path('politicasCyD/',vistas.renderPoliticasCyD),
    path('politicasP/',vistas.renderPoliticasP),
    path('condicionesD/',vistas.renderCondicionesD),
    path('productos/<int:categoria_id>/',vistas.renderProductos,name='productos'),
    path('producto/<int:producto_id>/', vistas.renderProducto, name='detalle_producto'),
    path('login/', vistas.iniciar_sesion,name='login'),
    path('registro/', vistas.registro,name='registro'),
    path('pago/', vistas.renderPago),
    path('carro/', vistas.renderCarro,name='carro'),
    path('despacho/', vistas.renderDespacho),
    path('categoria/<int:marca_id>/', vistas.marca,name='marca'),
    path('agregar/<int:producto_id>/', vistas.agregar_al_carrito, name='agregar_al_carrito'),
    path('crear_pedido/', vistas.crear_pedido, name='crear_pedido'),
    path('cerrar_sesion/',vistas.cerrar_sesion, name="cerrar_sesion"),
    path('d/',vistas.renderd)
]
