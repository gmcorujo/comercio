from django.db import models
# Create your models here.

class cliente(models.Model):
	def url(self,filename):
		ruta = "MiltimediaData/Cliente/%s/%s"%(self.nombre,str(filename))
		return ruta

	razonsocial			= models.CharField(max_length=60)
	domicilio			= models.CharField(max_length=50)
	status				= models.BooleanField(default=True)
	tipo_documento		= models.CharField(max_length=30)
	num_documento		= models.BigIntegerField()
	provincia			= models.CharField(max_length=50)
	localidad			= models.CharField(max_length=50)
	cuenta_corrinte		= models.BooleanField(default=False)
	limite_credito		= models.DecimalField(max_digits=6,decimal_places=2)
	plazo				= models.DateField()
	imagen				= models.ImageField(upload_to=url,null=True,blank=True)
	
	def __unicode__(self):
		return self.razonsocial

class empresa(models.Model):
	razon_social	= models.CharField(max_length=50)
	nombre_fantasia	= models.CharField(max_length=50)
	domicilio		= models.CharField(max_length=70)
	cuit			= models.CharField(max_length=30)
	localidad		= models.CharField(max_length=50)
	telefono		= models.CharField(max_length=30)

	def __unicode__(self):
		return self.razon_social

class proveedor(models.Model):
	razon_social		= models.CharField(max_length=60)
	nombre_fantasia		= models.CharField(max_length=60)
	domicilio			= models.CharField(max_length=100)
	status				= models.BooleanField(default=True)
	numero_cuit			= models.CharField(max_length=30)
	provincia			= models.CharField(max_length=50)
	localidad			= models.CharField(max_length=50)
	telefono			= models.CharField(max_length=30)

	def __unicode__(self):
		return self.razon_social

class rubroProducto(models.Model):
	nombre			= models.CharField(max_length=70)
	descripcion		= models.TextField(max_length=500)

	def __unicode__(self):
		return self.nombre

class marcaProducto(models.Model):
	nombre			= models.CharField(max_length=70)
	descripcion		= models.TextField(max_length=200)

	def __unicode__(self):
		return self.nombre

class producto(models.Model):
	def url(self,filename):
		ruta = "MiltimediaData/Producto/%s/%s"%(self.nombre,str(filename))
		return ruta

	nombre			= models.CharField(max_length=50)
	descripcion		= models.TextField(max_length=300)
	status			= models.BooleanField(default=True)
	imagen			= models.ImageField(upload_to=url,null=True,blank=True)
	stock			= models.DecimalField(max_digits=6,decimal_places=2)
	precio_costo	= models.DecimalField(max_digits=6,decimal_places=2)
	precio_venta	= models.DecimalField(max_digits=6,decimal_places=2)
	rubro 			= models.ManyToManyField(rubroProducto,null=True,blank=True)
	marca 			= models.ManyToManyField(marcaProducto,null=True,blank=True)
	proveedor		= models.ManyToManyField(proveedor,null=False,blank=False)
	
	def __unicode__(self):
		return self.nombre