
ENVIROMENT_DEBUG = "http://localhost:9090"
ENVIROMENT_PRODUCTION = "http://apinvoice.pythonanywhere.com"

ENVIROMENT = ENVIROMENT_DEBUG

VALIDATE_LOGIN = ENVIROMENT+"/employee/Validate_Login/"
GET_LIST_CLIENT = ENVIROMENT+"/client/GET_LIST_CLIENT/"
GET_CLIENT = ENVIROMENT+"/client/GET_CLIENT/"
GET_PRODUCT = ENVIROMENT+"/inventory/GET_PRODUCT/"
GET_LIST_INVENTORY = ENVIROMENT+"/inventory/GET_LIST_INVENTORY/"
CREATE_INVOICE = ENVIROMENT+"/invoice_fe/CREATE_INVOICE/"
GET_LIST_INVOICE = ENVIROMENT+"/invoice_fe/GET_LIST_INVOICE/"
GET_LIST_EMPLOYEE = ENVIROMENT+"/employee/GET_LIST_EMPLOYEE/"
# SEND_DIAN = ENVIROMENT+"/employee/Send_DIAN/"
SEND_DIAN = ENVIROMENT+"/invoice_fe/Send_DIAN/"


FILE_JSON_INVOICE_FE = "./static/data_fe.json"
FILE_JSON_INVOICE_POS = "./static/data_pos.json"
FILE_JSON_EARRING = "./static/earring.json"
FILE_JSON_CLIENTS = "./static/clients.json"
FILE_JSON_INVENTORY = "./static/inventory.json"
FILE_JSON_TYPE_DOCUMENTI = "./static/type_documentI.json"