from query_invoice import Query_Invoice
from django.shortcuts import render
import json,env
from query_client import Query_Client

def Index(request):
	query = Query_Invoice()
	list_invoice = query.GET_LIST_INVOICE(request,1)
	with open(env.FILE_JSON_INVOICE_FE, 'w') as file:
		json.dump(list_invoice, file, indent=4)
	list_invoice = query.GET_LIST_INVOICE(request,2)
	with open(env.FILE_JSON_INVOICE_POS, 'w') as file:
		json.dump(list_invoice, file, indent=4)
	list_invoice = Query_Client().GET_LIST_CLIENT(request)
	with open(env.FILE_JSON_CLIENTS, 'w') as file:
		json.dump(list_invoice, file, indent=4)
	del query
	del list_invoice
	return render(request,'index.html')