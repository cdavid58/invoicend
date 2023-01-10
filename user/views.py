from django.http import HttpResponse
from django.shortcuts import render
from .query_api import Query_API
import json, requests



def Login(request):
	if request.is_ajax():
		data = request.GET
		q = Query_API()
		result = q.validate_login(data,request)
		del q
		return HttpResponse(result)
	return render(request,'login.html')

def Add_Employee(request):
	if request.is_ajax():
		data = request.data

		return HttpResponse(True)
	return render(request,'inventory/add.html')


def GET_LIST_EMPLOYEE(request):
	url = "http://localhost:9090/employee/GET_LIST_EMPLOYEE/"
	payload = json.dumps({
	  "company": request.session['company_pk']
	})
	headers = {
	  'Content-Type': 'application/json'
	}
	response = requests.request("POST", url, headers=headers, data=payload)
	result = json.loads(response.text)
	return render(request,'employee/list_employee.html',{'employee':result})

def GET_EMPLOYEE(request,pk):
	if request.is_ajax():
		print(request.GET)
		# with open(request.FILES['img'], "rb") as image_file:
		# 	data = base64.b64encode(image_file.read())
		# print(data)
		return HttpResponse()


	url = "http://localhost:9090/employee/GET_EMPLOYEE/"
	payload = json.dumps({
	  "pk_employee": 1
	})
	headers = {
	  'Content-Type': 'application/json'
	}
	response = requests.request("POST", url, headers=headers, data=payload)
	employee = json.loads(response.text)
	return render(request,'employee/profile.html',{'employee':employee})

