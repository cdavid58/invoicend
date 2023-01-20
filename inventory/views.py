from django.http import HttpResponse
from django.shortcuts import render
import json,env, threading, queue, requests, urllib
from query_inventory import Query_Inventory

enviroments_json = env.ENVIROMENT_JSON

def List_Inventory(request):
	print(request.session['type_employee'])
	return render(request,'inventory/list_inventory.html',{'json':enviroments_json+"/static/inventory.json"})

def Add_Product(request):
	return render(request,'inventory/add.html')

def Edit_Product(request,pk):
	with open(env.FILE_JSON_INVENTORY) as file:
		data = json.load(file)
	product = None
	request.session['pk_product'] = pk
	for i in data:
		if str(pk) == str(i['pk']):
			product = i
			break
	return render(request,'inventory/edit.html',{'p':product})

def UPDATED_PRODUCT(request):
	if request.is_ajax():
		data = request.GET
		_data = {
	    "pk":request.session['pk_product'],
	    "name":data['name'],
	    "tax":data['tax'],
	    "cost":data['quanty'],
	    "price_1":data['price_1'],
	    "price_2":data['price_2'],
	    "price_3":data['price_3'],
	    "price_4":data['price_4'],
	    "price_5":data['price_5'],
	    "company":request.session['company_pk']
		}
		del request.session['pk_product']
		result = Query_Inventory().UPDATED_PRODUCT(_data)
		message = result['message']
		if result['result']:
			message = result['message']
			u = threading.Thread(target=Refresh_List_Inventory,args=(request,), name='Invoice')
			u.start()
		return HttpResponse(result['result'])		

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
		result = Query_Inventory().CREATE_PRODUCT(request,data)
		u = threading.Thread(target=Refresh_List_Inventory,args=(request,), name='Invoice')
		u.start()
		return HttpResponse(result)

def DELETE_PRODUCT(request):
	if request.is_ajax():
		data = request.GET
		_data = {
			'company':request.session['company_pk'],
			'code':data['code']
		}
		result = Query_Inventory().DELETE_PRODUCT(_data)
		list_inventory = Query_Inventory().GET_LIST_INVENTORY(request)
		with open(env.FILE_JSON_INVENTORY, 'w') as file:
			json.dump(list_inventory, file, indent=4)
		return HttpResponse(result)
