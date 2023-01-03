from django.shortcuts import render
import env, json, requests

class Query_Client:
	def GET_LIST_CLIENT(self,request):
		url = env.GET_LIST_CLIENT
		payload = json.dumps({
		  "company": request.session['company_pk']
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)['client']

	def GET_CLIENT(self,request):
		url = env.GET_CLIENT
		payload = json.dumps({
		  "pk": request.GET['pk']
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		client = json.loads(response.text)['client']
		request.session['pk_client'] = client['pk']
		return json.dumps(client)
		
	def GET_CONSECUTIVE(self,request):
		url = "http://localhost:9090/invoice_fe/GET_CONSECUTIVE/"
		payload = json.dumps({
		  "company":request.session['company_pk'],
		  "type_invoice":request.session['type_invoice']
		})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)['consecutive']

	def DELETE_CLIENT(self,data):
		url = "http://localhost:9090/client/DELETE_CLIENT/"
		payload = json.dumps({
			'pk':data['pk']
		})
		print(payload)
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)['client']

	def CREATE_CLIENT(self,request,data):
		url = "http://localhost:9090/client/CREATE_CLIENT/"
		payload = json.dumps({
		  "identification_number": data['docI'],
		  "dv": data['docI'][-1],
		  "name": data['name'],
		  "phone": data['phone'] if data['phone'] != "" else None,
		  "address": data['address'] if data['address'] != "" else None,
		  "email": data['email'] if data['email'] != "" else None,
		  "merchant_registration": None,
		  "type_documentI": data['type_document'],
		  "type_organization": data['organization'],
		  "type_regime": data['regime'],
		  "municipality": data['municipality'],
		  "company": request.session['company_pk']
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)['Result']

