import json, requests
import env

class Query_API:
	def validate_login(self,data,request):
		url = env.VALIDATE_LOGIN
		payload = json.dumps({
		  "user": data['user'],
		  "psswd": data['psswd']
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		result = json.loads(response.text)
		if result['result']:
			request.session['name_user'] = data['user']
			request.session['employee_pk'] = result['employee']
			request.session['company_pk'] = result['company']
		return result['result']
