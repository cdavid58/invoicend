from django.http import HttpResponse
from django.shortcuts import render
import json,env, threading, queue, requests
from query_inventory import Query_Inventory

def List_Inventory(request):
	return render(request,'inventory/list_inventory.html',{'json':"http://localhost:8000/static/inventory.json"})

def Add_Product(request):
	return render(request,'inventory/add.html')

my_queue = queue.Queue()
def storeInQueue(f):
  def wrapper(*args):
  	global my_queue
  	my_queue.put(f(*args))
  return wrapper

@storeInQueue
def Refresh_List_Inventory(request):
	list_inventory = Query_Inventory().GET_LIST_INVENTORY(request)
	with open(env.FILE_JSON_INVENTORY, 'w') as file:
		json.dump(list_inventory, file, indent=4)

def Save_Product(request):
	if request.is_ajax():
		data = request.GET
		url = "http://localhost:9090/inventory/CREATE_INVENTORY/"
		payload = json.dumps({
		  "code": data['code'],
		  "name": data['name'],
		  "quanty": data['quanty'],
		  "tax": data['tax'],
		  "cost": data['cost'],
		  "price_1": data['price_1'],
		  "price_2": data['price_2'],
		  "price_3": data['price_3'],
		  "price_4": data['price_4'],
		  "price_5": data['price_5'],
		  "supplier": 1,
		  "subcategory": 1,
		  "company": request.session['company_pk']
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		print(response.text)
		u = threading.Thread(target=Refresh_List_Inventory,args=(request,), name='Invoice')
		u.start()
		return HttpResponse(data)

