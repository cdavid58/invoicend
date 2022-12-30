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


def Create_Invoice_POS(request):
	request.session['type_invoice'] = 2
	qc = Query_Client()
	query = qc.GET_LIST_CLIENT(request)
	consecutive = qc.GET_CONSECUTIVE(request)
	del qc
	request.session['payment_form'] = 1
	request.session['date_expired'] = str(date.today())
	return render(request,'invoice/create_invoice.html',{'client':query,'type_invoice':'POS','consecutive':consecutive})

def GET_LIST_INVOICE_POS(request):
	request.session['type_invoice'] = 2
	return render(request,'list_invoice/invoice.html',{'json':'data_pos.json'})





