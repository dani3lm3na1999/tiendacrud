from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm

# existen 2 tipos de parametros que se usan en las peticiones http 
# 1- Request
# 2- Response
# Create your views here.
def hola_mundo(request):
    return HttpResponse('<h2>Hola Mundo desde Django</h2><br><p>Clase Semana 10</p>')

def inicio(request):
    return render(request, 'pages/inicio.html')

def listado_productos(request):
    # primero creamos una variable para almacenar los productos
    productos = Producto.objects.all()
    return render(request, 'producto/productos.html', { 'productos': productos })

def crear_producto(request):
    formulario = ProductoForm(request.POST or None)

    if formulario.is_valid():
        # producto = formulario.save(commit=False)
        formulario.save()
        return redirect('productos')
    
    return render(request, 'producto/crear.html', {'formulario': formulario})
    
def editar_producto(request, id):
    producto = Producto.objects.get(id = id)

    formulario = ProductoForm(request.POST or None, instance = producto)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    
    return render(request, 'producto/editar.html', {'formulario': formulario})

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('productos')

    