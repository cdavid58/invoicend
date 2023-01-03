from django.http import HttpResponse
from django.shortcuts import render
from query_client import Query_Client
import requests,json

def List_Client(request):
	return render(request,'client/list_client.html',{'json':"http://localhost:8000/static/clients.json"})

def Add_Client(request):
	return render(request,'client/add.html',{
		'Type_DocumentI':Type_DocumentI(),
		'Type_Organizations':Type_Organizations(),
		'Type_Regimen':Type_Regimen(),
		'Municipalitys':Municipalitys()
	})

def CREATE_CLIENT(request):
	if request.is_ajax():
		data = request.GET
		query = Query_Client().CREATE_CLIENT(request,data)
	return HttpResponse(True)

def DELETE_CLIENT(request):
	if request.is_ajax():
		if Query_Client().DELETE_CLIENT(request.GET):
			list_invoice = Query_Client().GET_LIST_CLIENT(request)
			with open(env.FILE_JSON_CLIENTS, 'w') as file:
				json.dump(list_invoice, file, indent=4)
		return HttpResponse(True)



def Type_DocumentI():
	url = "http://localhost:9090/settings/Type_DocumentI/"
	payload = json.dumps({})
	headers = {'Content-Type': 'application/json'}
	response = requests.request("POST", url, headers=headers, data=payload)
	return json.loads(response.text)

def Type_Organizations():
	url = "http://localhost:9090/settings/Type_Organizations/"
	payload = json.dumps({})
	headers = {'Content-Type': 'application/json'}
	response = requests.request("POST", url, headers=headers, data=payload)
	return json.loads(response.text)

def Type_Regimen():
	url = "http://localhost:9090/settings/Type_Regimen/"
	payload = json.dumps({})
	headers = {'Content-Type': 'application/json'}
	response = requests.request("POST", url, headers=headers, data=payload)
	return json.loads(response.text)

def Municipalitys():
	url = "http://localhost:9090/settings/Municipalitys/"
	payload = json.dumps({})
	headers = {'Content-Type': 'application/json'}
	response = requests.request("POST", url, headers=headers, data=payload)
	return json.loads(response.text)

