from django.shortcuts import render
import env, json, requests

class Create_Invoice:
	def __init__(self,request,data):
		self.data = data
		self.request = request

	def Send_Invoice(self):
		url = env.CREATE_INVOICE
		payload = json.dumps(self.data)
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		self.data = response.text
		if self.request.session['type_invoice'] == 1:
			self.Save_Record_JSON(env.c)		
		else:
			self.Save_Record_JSON(env.FILE_JSON_INVOICE_POS)	
		return True 

	def Save_Record_JSON(self,file_information):
		with open(file_information) as file:
			data = json.load(file)
		data.append(json.loads(self.data))
		with open(file_information, 'w') as file:
			json.dump(data, file, indent=4)

	def Send_Invoice_Dian(self,consecutive):
		url = "http://localhost:9090/invoice_fe/Send_DIAN/"
		payload = json.dumps({
		  "consecutive": consecutive
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		with open(env.FILE_JSON_INVOICE) as file:
			data = json.load(file)

		result = json.loads(response.text)['Result']

		for i in range(len(data)):
			if int(data[i]['consecutive']) == int(consecutive):
				data[i]['state'] = result
		with open(env.FILE_JSON_INVOICE, 'w') as file:
			json.dump([], file, indent=4)

		with open(env.FILE_JSON_INVOICE, 'w') as file:
			json.dump(data, file, indent=4)

		return result



class Query_Invoice:
	def GET_LIST_INVOICE(self,request,type_invoice):
		url = env.GET_LIST_INVOICE
		payload = json.dumps({
		  "company": request.session['company_pk'],
		  "type":type_invoice
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)


	def GET_INVOICE(self,pk,request):
		url = "http://localhost:9090/invoice_fe/GET_INVOICE/"
		payload = json.dumps({
		  "company":request.session['company_pk'],
		  "consecutive": pk,
		  "type_invoice":request.session['type_invoice']
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)


	