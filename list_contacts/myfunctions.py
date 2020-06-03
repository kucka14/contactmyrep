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
	
	officeid_list = []
	for div in data5["divisions"].keys():
		if data5["divisions"][div]["name"] != "United States":
			try:
				officeid_list = officeid_list + data5["divisions"][div]["officeIndices"]
			except:
				pass
	
	officeid_list.sort()
		
	rep_dict = {}   
		
	for officeid in officeid_list:
		for officialid in data5["offices"][officeid]["officialIndices"]:
			rep_dict[officialid] = {}
			
			display_list = [["level","levels"],["office","name"]]
			for item in display_list:
				try:
					rep_dict[officialid][item[0]] = data5["offices"][officeid][item[1]]           
				except:
					pass
			
			display_list = [["name","name"],["photo","photoUrl"],["phone","phones"],["email","emails"]]
			for item in display_list:
				try:
					rep_dict[officialid][item[0]] = data5["officials"][officialid][item[1]]           
				except:
					pass
		
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
	
def split_rep_list(rep_list):
	
	level_dict = {
		"international":0,
		"country":1,
		"administrativeArea1":2,
		"administrativeArea2":3,
		"locality":4,
		"subLocality1":5,
		"subLocality2":6,
		"special":7,
		"regional":8
	}
	
	rep_list_spl = [
					{"banner":"International","display":[]},
					{"banner":"Federal","display":[]},
					{"banner":"State","display":[]},
					{"banner":"County","display":[]},
					{"banner":"City","display":[]},
					{"banner":"Local","display":[]},
					{"banner":"Neighborhood","display":[]},
					{"banner":"Special","display":[]},
					{"banner":"Regional","display":[]},
					{"banner":"Other","display":[]},
					]
	
	for rep in rep_list:
		level_word = rep["level"][0]
		try:
			level_int = level_dict[level_word]
		except:
			level_int = 9
		rep["level"] = level_int
		
		index = rep["level"]
		
		rep_list_spl[index]["display"].append(rep)
		
	rep_list_split = [x for x in rep_list_spl if len(x["display"]) != 0]
		
	return rep_list_split
	

	
	
	
	
	
	
	
	
	
	
