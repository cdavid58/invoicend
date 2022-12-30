from django.shortcuts import render
from django.http import HttpResponse
from query_client import Query_Client
from query_inventory import Query_Inventory
from query_invoice import Create_Invoice,Query_Invoice
import json, threading, queue
from date import Count_Days
from datetime import date
from from_number_to_letters import Thousands_Separator

my_queue = queue.Queue()

def storeInQueue(f):
  def wrapper(*args):
  	global my_queue
  	my_queue.put(f(*args))
  return wrapper


def Create_Invoice_FE(request):
	request.session['type_invoice'] = 1
	qc = Query_Client()
	query = qc.GET_LIST_CLIENT(request)
	consecutive = qc.GET_CONSECUTIVE(request)
	del qc
	request.session['payment_form'] = 1
	request.session['date_expired'] = str(date.today())
	return render(request,'invoice/create_invoice.html',{'client':query,'type_invoice':'Electrónica','consecutive':consecutive})

def GET_CLIENT(request):
	if request.is_ajax():
		qc = Query_Client()
		query = qc.GET_CLIENT(request)
		del qc
		return HttpResponse(query)

def GET_PRODUCT(request):
	if request.is_ajax():
		qi = Query_Inventory()
		query = qi.GET_PRODUCT(request)
		del qi
		return HttpResponse(query)

def Set_Payment_Form(request):
	if request.is_ajax():
		request.session['payment_form'] = int(request.GET['pk'])
		return HttpResponse(True)

def Date_Expired(request):
	if request.is_ajax():
		print('FECHA')
		date = request.GET['date_expired'].split('-')[1].strip()
		print(date)
		request.session['date_expired'] = date
		return HttpResponse(True)		

def Save_Invoice(request):
	if request.is_ajax():
		data = request.GET
		_data = None
		for i in data:
			_data = json.loads(i)
		_data[0]['type'] = request.session['type_invoice']
		payment_form = request.session['payment_form']
		_data[0]['payment_form'] = payment_form
		if payment_form == 1:
			_data[0]['cancelled'] = True
		else:
			_data[0]['cancelled'] = False
		_data[0]['employee'] = request.session['employee_pk']
		_data[0]['client'] = request.session['pk_client']
		_data[0]['company'] = request.session['company_pk']
		_data[0]['date'] = str(date.today())
		_data[0]['date_expired'] = request.session['date_expired']
		_data[0]['time'] = "21:45"
		c = Create_Invoice(request,_data)
	return HttpResponse(c.Send_Invoice())



def GET_LIST_INVOICE(request):
	request.session['type_invoice'] = 1
	return render(request,'list_invoice/invoice.html',{'json':'data_fe.json'})

def View_Invoice(request,pk):
	query = Query_Invoice()
	data = query.GET_INVOICE(pk,request)
	details_product = data['product']
	informations = data['information']
	client = data['client']
	subtotal_invoice = 0
	tax_invoice = 0
	for i in details_product:
		subtotal_invoice += i['subtotal']
		tax_invoice += i['val_tax']
	total = subtotal_invoice + tax_invoice
	del query
	date_ = str(informations['date_expired'])
	_date = date_.split('-')
	dates = list(map(int, _date))
	days = Count_Days(dates)
	if informations['payment_form'] == "Contado":
		days = 0
	type_invoice = "Electrónica"
	if request.session['type_invoice'] == 2:
		type_invoice = "POS"

	return render(request,'list_invoice/view_invoice.html',{'details_product':details_product,'total':Thousands_Separator(total), 
		'subtotal_invoice':Thousands_Separator(subtotal_invoice),'tax_invoice':Thousands_Separator(tax_invoice), 'iva19':VALUES_TAXES(19,details_product),
		'iva5':VALUES_TAXES(5,details_product), 'iva0':VALUES_TAXES(0,details_product), 'client':client, 'information':informations, 'days_expired':days,'type_invoice':type_invoice})

def VALUES_TAXES(tax,data):
	total_base = 0
	total_tax = 0
	for i in data:
		if tax == i['tax']:
			total_base += i['price_base']
			total_tax = i['val_tax']
	return {str(tax):total_tax,'base':total_base}


def Send_DIAN(request):
	if request.is_ajax:
		consecutive = request.GET['consecutive']
		u = threading.Thread(target=Send_Invoice,args=(consecutive,), name='Invoice')
		u.start()
		data = my_queue.get()
	return HttpResponse(data)

@storeInQueue
def Send_Invoice(consecutive):
	ci = Create_Invoice('')
	return ci.Send_Invoice_Dian(consecutive)
	
	

