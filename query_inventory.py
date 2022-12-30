from django.shortcuts import render
import env, json, requests

class Query_Inventory:

	def GET_PRODUCT(self,request):
		url = env.GET_PRODUCT
		payload = json.dumps({
		  "value": request.GET['value']
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		product = json.loads(response.text)
		return json.dumps(product)

	def GET_LIST_INVENTORY(self):
		url = env.GET_LIST_INVENTORY
		payload = json.dumps({
		  "company": 20302968
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)

