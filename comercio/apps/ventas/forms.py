from django import forms

class addProductForm(forms.Form):
	nombre      	= forms.CharField(widget=forms.TextInput())
	descripcion 	= forms.CharField(widget=forms.TextInput())
	imagen			= forms.ImageField(required=False)
	stock			= forms.DecimalField(required=True)
	precio_costo	= forms.DecimalField(required=True)
	precio_venta	= forms.DecimalField(required=True)
	

	def clean(self):
		return self.cleaned_data


class addRubroForm(forms.Form):
	nombre			= forms.CharField(widget=forms.TextInput())
	descripcion		= forms.CharField(widget=forms.TextInput())

	def clean(self):
		return self.cleaned_data

class addMarcaForm(forms.Form):
	nombre			= forms.CharField(widget=forms.TextInput())
	descripcion		= forms.CharField(widget=forms.TextInput())

	def clean(self):
		return self.cleaned_data