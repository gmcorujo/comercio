# Create your views here.
from django.shortcuts 				import render_to_response
from django.template 				import RequestContext
from comercio.apps.ventas.forms 	import addProductForm, addRubroForm, addMarcaForm
from comercio.apps.ventas.models 	import producto, rubroProducto, marcaProducto
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


def add_rubro_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addRubroForm(request.POST)
			info = "Inicializando"
			if form.is_valid():
				nombre			= form.cleaned_data['nombre']
				descripcion		= form.cleaned_data['descripcion']
				r = rubroProducto()
				r.nombre		= nombre
				r.descripcion	= descripcion
				r.save()
				info = "El Rubro se Guardo Correctamente"
			else:
				info = "Informacion con datos de Rubros Incorrectos"
			form = addRubroForm()
			ctx  = {'form':form, 'informacion':info}
			return render_to_response('ventas/addRubro.html',ctx,context_instance=RequestContext(request))
		else: #GET
			form = addRubroForm()
			ctx  = {'form':form}
			return render_to_response('ventas/addRubro.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

def add_marca_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addMarcaForm(request.POST)
			info = "Inicializando"
			if form.is_valid():
				nombre			= form.cleaned_data['nombre']
				descripcion		= form.cleaned_data['descripcion']
				m = marcaProducto()
				m.nombre 		= nombre
				m.descripcion	= descripcion
				m.save()
				info 	= "La Marca se Guardo Correctamente"
			else:
				info = "Informacion con datos de Marca Incorrectos"
			form = addMarcaForm()
			ctx  = {'form':form, 'informacion':info}
			return render_to_response('ventas/addMarca.html',ctx,context_instance=RequestContext(request))
		else:
			form = addMarcaForm()
			ctx  = {'form':form}
			return render_to_response('ventas/addMarca.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')