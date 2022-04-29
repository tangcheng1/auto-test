# import json
# from config.config import *
# import requests
#
# from tools import  base_requests
# from tools.base_requests import excel_read
#
# a = excel_read()
#
# # print (a)
#
#
# for i in a :
#     api = i.get("url")
#     headers = i.get("headers")
#     method = i.get("method")
#     data = i.get("data")
#     url = URL+api
#     print(url)
#     print(headers)
#     print(type(json.dumps(headers)))
#     print(data)
    # response = requests.post(url=url, data=json.dumps(data), headers=json.dumps(headers))
    # if  method == "post":
    #     response = requests.post(url=url, data=json.dumps(data), headers=json.dumps(headers))
    #     print("post请求"+response.json())
    # else:
    #     response = requests.get(url=url, data=json.dumps(data)headers=json.dumps(headers))
    #     print("get请求"+response.json())