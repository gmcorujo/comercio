# Create your views here.
from django.shortcuts 				import render_to_response
from django.template 				import RequestContext
from comercio.apps.ventas.models 	import producto,proveedor,empresa
from comercio.apps.home.forms 		import ContactForm,LoginForm

from django.contrib.auth 			import login,logout,authenticate
from django.http					import HttpResponseRedirect
def index_view(request):
	return render_to_response('home/index.html', context_instance=RequestContext(request))

def about_view(request):
	mensaje = "Esto es un mensaje desde mi vista!!"
	ctx 	= {'msg':mensaje}
	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def empresa_view(request):
	emp = empresa.objects.all()
	ctx = {'empresa':emp}
	return render_to_response('home/empresa.html',ctx,context_instance=RequestContext(request))

def productos_view(request):
	prod 	= producto.objects.filter(status=True) #Es igual a --> SELECT *FROM ventas_productos where status = True
	ctx 	= {'productos': prod}
	return render_to_response('home/productos.html',ctx,context_instance=RequestContext(request))

def proveedor_view(request):
	prov = proveedor.objects.filter(status=True)
	ctx  = {'proveedor':prov}
	return render_to_response('home/proveedores.html',ctx,context_instance=RequestContext(request))

def singleProducto_view(request,id_prod):
	prod 	= producto.objects.get(id=id_prod)
	ctx 	= {'producto':prod}
	return render_to_response('home/singleproducto.html',ctx,context_instance=RequestContext(request))

def contacto_view(request):
	info_enviado	= False
	email	= ""
	titulo	= ""
	texto	= ""
	if request.method == "POST":
		formulario	= ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado 	= True
			email 		= formulario.cleaned_data['Email']
			titulo		= formulario.cleaned_data['Titulo']
			texto 		= formulario.cleaned_data['Texto']
	else:
		formulario = ContactForm()

	ctx = {'form':formulario, 'email':email, 'titulo':titulo, 'texto':texto,'info_enviado':info_enviado}
	return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))
 

def login_view(request):
	mensaje =""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else: 
					mensaje = "Usuario y/o Password incorrectos!"
		form = LoginForm()
		ctx = {'form':form,'mensaje':mensaje}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

