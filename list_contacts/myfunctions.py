import requests
import json

def make_rep_list(address):
	params = {
		'key':'AIzaSyAAcFl9TBF2bFcezo8J1pguPSLbmVy7bmY',
		'address':address,
		}
	url = "https://www.googleapis.com/civicinfo/v2/representatives"
	data0 = requests.get(url,params)
	data5 =  data0.json()
	
	div_list = []
	for div in data5["divisions"].keys():
		try:
			div_list.append(data5["divisions"][div]["officeIndices"])  
		except:
			pass
	div_list.sort() 
		
	rep_dict = {}   
		
	division_count = 0
	for division in div_list:
		for officeid in division:
			for officialid in data5["offices"][officeid]["officialIndices"]:
				rep_dict[officialid] = {}
				rep_dict[officialid]["division"] = str(division_count)
				
				try:
					rep_dict[officialid]["office"] = data5["offices"][officeid]["name"]
				except:
					pass
				
				display_list = [["name","name"],["photo","photoUrl"],["phone","phones"],["email","emails"]]
				for item in display_list:
					try:
						rep_dict[officialid][item[0]] = data5["officials"][officialid][item[1]]           
					except:
						pass
		division_count += 1
		
		rep_list = map_to_list(rep_dict)
				
	return rep_list
	
def make_raw_data(address):
	params = {
	'key':'AIzaSyAAcFl9TBF2bFcezo8J1pguPSLbmVy7bmY',
	'address':address,
	}
	url = "https://www.googleapis.com/civicinfo/v2/representatives"
	data0 = requests.get(url,params)
	data5 =  data0.json()
	
	return data5
	
def map_to_list(dictionary):

	dict_keys = list(dictionary.keys())
	dict_keys.sort()
	
	dict_list = []
	for key in dict_keys:
		dict_list.append(dictionary[key])
	
	return dict_list
	
def vdo(address,context):
	rep_list = make_rep_list(address)
	context['slide_dir'] = 'slide-up'
	context['display'] = 'show-div'
	
	return rep_list,context

def ivdo(context):
	context['slide_dir'] = 'slide-down'
	context['display'] = 'hide-div'
	rep_list = {}
	
	return rep_list,context
	
def add_contacts(rep_list,contact_dict):
	for rep in rep_list:
		name = rep["name"]
		if name in contact_dict.keys():
			rep["contact"] = contact_dict[name]
			
	return rep_list
	
	
	
	
	
	
	
	
	
