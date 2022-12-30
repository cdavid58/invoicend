from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^$',Login,name="Login"),
		url(r'^GET_LIST_EMPLOYEE/$',GET_LIST_EMPLOYEE,name="GET_LIST_EMPLOYEE"),
		url(r'^GET_EMPLOYEE/(\d+)/$',GET_EMPLOYEE,name="GET_EMPLOYEE"),
	]