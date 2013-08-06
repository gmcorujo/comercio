# Create your views here.
from django.shortcuts 				import render_to_response
from django.template 				import RequestContext
from comercio.apps.ventas.forms 	import addProductForm
from comercio.apps.ventas.models 	import producto
from django.http 					import HttpResponseRedirect

def add_product_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addProductForm(request.POST, request.FILES)
			info = "Inicializando"
			if form.is_valid():
				nombre 			= form.cleaned_data['nombre']
				descripcion 	= form.cleaned_data['descripcion']
				imagen			= form.cleaned_data['imagen'] # Esto se obtiene con el request.FILES
				stock			= form.cleaned_data['stock']
				precio_costo	= form.cleaned_data['precio_costo']
				precio_venta	= form.cleaned_data['precio_venta']
				p = producto()
				if imagen: # Genero una validacion
					p.imagen = imagen 
				p.nombre 		= nombre
				p.descripcion 	= descripcion
				p.stock			= stock
				p.precio_costo	= precio_costo
				p.precio_venta	= precio_venta
				p.status = True
				p.save() # Guarda la Informacion
				info = "Se guardo satisfactoriamente!!"
			else:
				info = "Informacion con datos incorrectos"
			form = addProductForm()
			ctx = {'form':form,'informacion':info}
			return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
		else:# GET
			form = addProductForm()
			ctx  = {'form':form}
			return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')