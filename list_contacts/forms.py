from django import forms

class AddressForm(forms.Form):
	address = forms.CharField(widget=forms.TextInput(attrs={'id':'address',
							  								'placeholder':'Enter your home address',
							  								'onFocus':'geolocate()',
							  								'class':'form-control form-control-lg rep-form'
															}))
							  	               
