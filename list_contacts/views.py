from django.shortcuts import render

from .forms import AddressForm
from .myfunctions import make_rep_list,make_raw_data,vdo,ivdo,add_contacts,split_rep_list
from .contact_dict import contact_dict

import json

# Create your views here.

def index(request):

	form = AddressForm(request.GET)
	context = {}

	if form.is_valid():
		try:
			address = form.cleaned_data['address']
			rep_list,context = vdo(address,context)
			rep_list = add_contacts(rep_list,contact_dict)
			rep_list = split_rep_list(rep_list)
			
		except:
			rep_list,context = ivdo(context)
			context['errors'] = ['Please enter a valid address']
	else:
		form = AddressForm()
		rep_list,context = ivdo(context)
		
	return render(request, 'list_contacts/index.html', {'form':form,'rep_list':rep_list,'context':context})

def robots(request):
	return render(request, 'list_contacts/robots.txt')
	
def sitemap(request):
	return render(request, 'list_contacts/sitemap.xml')	

	
	
