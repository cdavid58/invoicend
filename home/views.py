from query_invoice import Query_Invoice
from django.shortcuts import render
import json, env, threading, queue, requests
from query_client import Query_Client
from query_inventory import Query_Inventory

my_queue = queue.Queue()
def storeInQueue(f):
  def wrapper(*args):
  	global my_queue
  	my_queue.put(f(*args))
  return wrapper


def Index(request):
	u = threading.Thread(target=Generated_File,args=(request,), name='Invoice')
	u.start()
	url = "http://localhost:9090/settings/Type_DocumentI/"
	payload = json.dumps({})
	headers = {'Content-Type': 'application/json'}
	response = requests.request("POST", url, headers=headers, data=payload)
	with open(env.file_json_type_documenti,'w') as file:
		json.dump(json.loads(response.text),file,indent=4)
	return render(request,'index.html')

@storeInQueue
def Generated_File(request):
	query = Query_Invoice()
	list_invoice_fe = query.GET_LIST_INVOICE(request,1)
	with open(env.FILE_JSON_INVOICE_FE, 'w') as file:
		json.dump(list_invoice_fe, file, indent=4)

	list_invoice_pos = query.GET_LIST_INVOICE(request,2)
	with open(env.FILE_JSON_INVOICE_POS, 'w') as file:
		json.dump(list_invoice_pos, file, indent=4)

	list_client = Query_Client().GET_LIST_CLIENT(request)
	with open(env.FILE_JSON_CLIENTS, 'w') as file:
		json.dump(list_client, file, indent=4)

	list_inventory = Query_Inventory().GET_LIST_INVENTORY(request)
	with open(env.FILE_JSON_INVENTORY, 'w') as file:
		json.dump(list_inventory, file, indent=4)

	# url = "http://localhost:9090/settings/Type_DocumentI/"
	# payload = json.dumps({})
	# headers = {'Content-Type': 'application/json'}
	# response = requests.request("POST", url, headers=headers, data=payload)
	# with open(env.file_json_type_documenti,'w') as file:
	# 	json.dump(json.loads(response.text),file,indent=4)
		
	del query
	del list_invoice