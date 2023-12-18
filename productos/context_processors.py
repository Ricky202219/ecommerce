from .models import Carrito, Categoria

def categorias(request):
    categorias = Categoria.objects.all()
    return {'categorias': categorias}  

# Importa tu modelo Carrito aquí

def carrito(request):
    if request.user.is_authenticated:
    # Obtén el carrito del usuario actual o crea uno si no existe
        carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    
    # Calcula el total del carrito
        total = carrito.total_carrito() if carrito.productos.exists() else 0
    
    # Retorna el contexto del carrito para estar disponible en todas las plantillas
        return {'carrito': carrito, 'total_carrito': total}
    else:
        total="Debes hacer login"
   
        
    return {"total_carrito":total}