# Create your views here.
from django.shortcuts 				import render_to_response
from django.template 				import RequestContext
from comercio.apps.ventas.forms 	import addProductForm, addRubroForm, addMarcaForm, addProveedorForm, addEmpresaForm, addClienteForm
from comercio.apps.ventas.models 	import producto, rubroProducto, marcaProducto, proveedor, empresa, cliente
from django.http 					import HttpResponseRedirect

def add_cliente_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addClienteForm(request.POST, request.FILES)
			info = "Inicializando"
			if form.is_valid():
				razonsocial 		= form.cleaned_data['razonsocial']
				domicilio			= form.cleaned_data['domicilio']
				tipo_documento		= form.cleaned_data['tipo_documento']
				num_documento		= form.cleaned_data['num_documento']
				provincia			= form.cleaned_data['provincia']
				localidad			= form.cleaned_data['localidad']
				limite_credito		= form.cleaned_data['limite_credito']
				plazo				= form.cleaned_data['plazo']
				imagen				= form.cleaned_data['imagen'] # Esto se obtiene con el request.FILES
				c = cliente()
				if imagen:
					c.imagen = imagen
				c.razonsocial 		= razonsocial
				c.domicilio			= domicilio
				c.tipo_documento	= tipo_documento
				c.num_documento		= num_documento
				c.provincia			= provincia
				c.localidad			= localidad
				c.cuenta_corrinte	= False
				c.status			= True
				c.limite_credito	= limite_credito
				c.plazo				= plazo
				c.save()
				info = "El Cliente se Guardo Correctamente"
			else:
				info = "El Cliente No se Guardo Correctamente"
			form = addClienteForm()
			ctx  = {'form':form, 'informacion':info}
			return render_to_response('ventas/addCliente.html',ctx,context_instance=RequestContext(request))
		else:
			form = addClienteForm()
			ctx  = {'form':form}
			return render_to_response('ventas/addCliente.html',ctx, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

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

def add_empresa_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addEmpresaForm(request.POST)
			info = "Inicializando"
			if form.is_valid():
				razon_social		= form.cleaned_data['razon_social']
				nombre_fantasia		= form.cleaned_data['nombre_fantasia']
				domicilio			= form.cleaned_data['domicilio']
				cuit 				= form.cleaned_data['cuit']
				localidad			= form.cleaned_data['localidad']
				telefono			= form.cleaned_data['telefono']
				emp = empresa()
				emp.razon_social		= razon_social
				emp.nombre_fantasia	= nombre_fantasia
				emp.domicilio			= domicilio
				emp.cuit 				= cuit
				emp.localidad			= localidad
				emp.telefono			= telefono
				emp.save()
				info = "La Empresa se Modifico Correctamente"
			else:
				info = "Informacion con datos incorrectos"
			form = addEmpresaForm()
			ctx  = {'form':form, 'informacion':info}	
			return render_to_response('ventas/addEmpresa.html',ctx,context_instance=RequestContext(request))
		else:
			form = addEmpresaForm()
			ctx  = {'form':form}
			return render_to_response('ventas/addEmpresa.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

def add_proveedor_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addProveedorForm(request.POST)
			info = "Inicializando"
			if form.is_valid():
				razon_social		= form.cleaned_data['razon_social']
				nombre_fantasia		= form.cleaned_data['nombre_fantasia']
				domicilio			= form.cleaned_data['domicilio']
				numero_cuit			= form.cleaned_data['numero_cuit']
				provincia			= form.cleaned_data['provincia']
				localidad			= form.cleaned_data['localidad']
				telefono			= form.cleaned_data['telefono']
				prov =proveedor()
				prov.razon_social	= razon_social
				prov.nombre_fantasia= nombre_fantasia
				prov.domicilio		= domicilio
				prov.numero_cuit	= numero_cuit
				prov.provincia		= provincia
				prov.localidad		= localidad
				prov.telefono		= telefono
				prov.save()
				info 				= "El Proveedor se Guardo Correctamente"
			else:
				info = "Informacion con datos incorrectos"
			form = addProveedorForm()
			ctx  = {'form':form, 'informacion':info}
			return render_to_response('ventas/addProveedor.html',ctx,context_instance=RequestContext(request))
		else:
			form = addProveedorForm()
			ctx  = {'form':form}
			return render_to_response('ventas/addProveedor.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')
