from django.shortcuts import render, get_object_or_404, redirect
from .models import Products
from .forms import ProductForm

def lista_products(request):
    products = Products.objects.all()
    
    return render(request, 'App/lista_productos.html', {'products': products})

def crear_product(request):
     if request.method == 'POST':
         form = ProductForm(request.POST)
         if form.is_valid():
             form.save()
             products = Products.objects.all()
             return render(request, 'App/lista_productos.html', {'products': products})
     else:
         form = ProductForm()
     return render(request, 'App/crear_producto.html', {'form': form})

# Vista para editar un product
def editar_producto(request, id):
    product = get_object_or_404(Products, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            products = Products.objects.all()
    
            return render(request, 'App/lista_productos.html', {'products': products})
    else:
        form = ProductForm(instance=product)
    return render(request, 'App/editar_producto.html', {'form': form})

# Vista para eliminar un product
def eliminar_producto(request, id):
    product = get_object_or_404(Products, id=id)
    if request.method == 'POST':
        product.delete()
        products = Products.objects.all()
        return render(request, 'App/lista_productos.html', {'products': products})
    return render(request, 'App/eliminar_producto.html', {'product': product})
