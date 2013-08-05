from django.contrib					import admin
from comercio.apps.ventas.models	import cliente, producto, proveedor, rubroProducto, marcaProducto, empresa

admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(proveedor)
admin.site.register(rubroProducto)
admin.site.register(marcaProducto)
admin.site.register(empresa)