from django.shortcuts import render
import env, json, requests

class Query_Inventory:

	def GET_PRODUCT(self,request):
		url = env.GET_PRODUCT
		payload = json.dumps({
		  "value": request.GET['value'],
		  "company":request.session['company_pk']
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		product = json.loads(response.text)
		return json.dumps(product)

	def GET_LIST_INVENTORY(self,request):
		url = env.GET_LIST_INVENTORY
		payload = json.dumps({
		  "company": request.session['company_pk']
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)

	def UPDATED_PRODUCT(self,data):
		url = env.UPDATED_PRODUCT
		payload = json.dumps(data)
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)

	def DELETE_PRODUCT(self,data):
		url = env.DELETE_PRODUCT
		payload = json.dumps(data)
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)['result']

	def CREATE_PRODUCT(self,request,data):
		url = env.CREATE_INVENTORY
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
		return json.loads(response.text)['Result']



