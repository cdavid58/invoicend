from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^List_Inventory/$',List_Inventory,name="List_Inventory"),
		url(r'^Add_Product/$',Add_Product,name="Add_Product"),
		url(r'^Save_Product/$',Save_Product,name="Save_Product"),
	]