from django.http import HttpResponse
from django.shortcuts import render
from query_client import Query_Client
import requests, json, env, threading, queue

my_queue = queue.Queue()

def storeInQueue(f):
  def wrapper(*args):
  	global my_queue
  	my_queue.put(f(*args))
  return wrapper

def List_Client(request):
	u = threading.Thread(target=GET_CLIENT_LIST,args=(request,), name='Invoice')
	u.start()
	return render(request,'client/list_client.html',{'json':"http://localhost:8000/static/clients.json"})

@storeInQueue
def GET_CLIENT_LIST(request):
	list_client = Query_Client().GET_LIST_CLIENT(request)
	with open(env.FILE_JSON_CLIENTS, 'w') as file:
		json.dump(list_client, file, indent=4)
	print(list_client)
	del list_client

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

