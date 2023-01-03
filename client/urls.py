from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^List_Client/$',List_Client,name="List_Client"),
		url(r'^Add_Client/$',Add_Client,name="Add_Client"),
		url(r'^CREATE_CLIENT/$',CREATE_CLIENT,name="CREATE_CLIENT"),
		url(r'^DELETE_CLIENT/$',DELETE_CLIENT,name="DELETE_CLIENT"),
	]