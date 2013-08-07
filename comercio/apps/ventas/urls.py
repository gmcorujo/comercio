from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('comercio.apps.ventas.views',
	url(r'^add/producto/$','add_product_view',name="vista_agregar_producto"),
	url(r'^add/rubro/$','add_rubro_view',name="vista_agregar_rubro"),
	url(r'^add/marca/$','add_marca_view',name="vista_agregar_marca"),
	url(r'^add/proveedor/$','add_proveedor_view',name="vista_agregar_proveedor"),
)
