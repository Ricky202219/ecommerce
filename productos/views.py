from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.csrf import csrf_protect
from .models import Producto, Categoria, Carrito, ItemCarrito, Pedido, DetallePedido,Marca
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroForm, LoginForm
from django.contrib import messages
# Create your views here.

def renderIndex(request):
    return render(request, 'home.html')

def renderTerminos(request):
    return render(request, 'terminos.html')

def renderPreguntas(request):
    return render(request, 'preguntas.html')

def renderPoliticasCyD(request):
    return render(request, 'politicas_cyd.html')

def renderPoliticasP(request):
    return render(request, 'politicas_p.html')

def renderCondicionesD(request):
    return render(request, 'condiciones_d.html')

def renderProductos(request, categoria_id):
    categoria_seleccionada = Categoria.objects.get(id=categoria_id)

    # Obtener las marcas asociadas a esa categoría
    marcas_por_categoria = Marca.objects.filter(categoria=categoria_seleccionada)

    # Obtener todos los productos de esas marcas asociadas a la categoría seleccionada
    productos = Producto.objects.filter(marca__in=marcas_por_categoria)

    return render(request, "menu_productos.html", {"productos": productos, "categorias": Categoria.objects.all(), "categoria_seleccionada": categoria_seleccionada, "marcas_por_categoria": marcas_por_categoria})

def renderProducto(request,  producto_id):
    producto = Producto.objects.get(pk=producto_id)
    return render(request, 'producto.html', {'producto': producto})

def renderLogin(request):
    return render(request, 'login.html')

def renderRegistro(request):
    return render(request, 'registro.html')

def renderPago(request):
    return render(request, 'pago.html')

def renderCarro(request):
    return render(request, 'carro.html')

def renderDespacho(request):
    return render(request, 'despacho.html')

def marca(request, marca_id):
    marca_seleccionada = get_object_or_404(Marca, id=marca_id)
    categoria_seleccionada = marca_seleccionada.categoria  # Obtener la categoría de la marca
    marcas_por_categoria = Marca.objects.filter(categoria=categoria_seleccionada)

    productos = Producto.objects.filter(marca=marca_seleccionada)

    return render(
        request,
        "marca.html",
        {
            "productos": productos,
            "marca_seleccionada": marca_seleccionada,
            "marcas": marcas_por_categoria,  # Pasar las marcas filtradas por categoría al template
        },
    )

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not creado:
        item.cantidad += 1
        item.save()
     # Obtener nuevamente los datos necesarios para la página
    # Aquí podrías obtener otros datos que se necesiten para la página
    return redirect(reverse('detalle_producto', args=[producto_id]))

def crear_pedido(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    # Crear un nuevo pedido
    pedido = Pedido.objects.create(usuario=request.user)
    # Transferir elementos del carrito al detalle del pedido
    
    items_carrito = carrito.itemcarrito_set.all()
    for item in items_carrito:
        DetallePedido.objects.create(pedido=pedido, producto=item.producto, cantidad=item.cantidad)
        pedido.save()

    carrito.itemcarrito_set.all().delete()
    
    # Redirigir o renderizar a otra página según sea necesario
    #return redirect('/')
    # O renderizar una página confirmando el pedido
    return render(request, 'home.html', {'pedido': pedido})


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autenticar al usuario recién registrado
            return redirect('/')  # Redirigir a la página principal después del registro
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Cambia 'index' por la URL a la que quieres redirigir después del inicio de sesión
            else:
                return redirect('/login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def cerrar_sesion(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    carrito.itemcarrito_set.all().delete()
    logout(request)

    return redirect('/')
