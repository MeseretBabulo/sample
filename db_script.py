import json
import logging
import requests
import werkzeug
import pprint

print("Script Running......")



# class GetStartScrip():
#     global private
#     global response

# def db_create_script(self):

print("Script Running......")

req_data = {"params" :{
    'master_pwd' : 'my_admin_passwd',
    'name': 'Script_DB',
    'lang': 'en_US',
    'login' :'admin', 
    'password': 'admin',
    'phone' : '0911223344', 
    'country_code' : 'et'
    } }

print(pprint.pformat(req_data))

_url = "http://127.0.0.1:8069/script/database/create/api" 

request_headers = {
        "Content-Type": "application/json",
}
    

try :
    response = requests.post(_url, headers=request_headers, json={}, data=json.dumps(req_data))
    print(response)
    print("_______________________________________")
  
except Exception as e:
    print(e)
if response.status_code == 200:
    print(
        'Success in post request, database is create from script')
    
    print(pprint.pformat(response))
    
