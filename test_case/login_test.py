# import requests
# import json
# from config.config import *
# import pytest
#
#
# def get_almightycode():
#     url = URL + "/api/admin/get/almighty/code"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) "
#                       "Chrome/54.0.2840.99 Safari/537.36"}
#     response = requests.get(url=url, headers=headers)
#     get_almightycode = response.json()["data"]
#     assert response.json()["code"] == "1"
#     return get_almightycode
#
#
# def login_test(smsCode):
#     smsCodenew = smsCode
#     params = {"smsCode": smsCodenew, "userName": "15400010001"}
#     url = URL + "/api/rider/smscode/login"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) "
#                       "Chrome/54.0.2840.99 Safari/537.36",
#         "deviceId": "123444",
#         'Content-Type': "application/json",
#         'Accept': "*/*"
#         }
#     response = requests.post(url=url, data=json.dumps(params), headers=headers)
#     get_logincode = response.json()["data"]["token"]
#     print(get_logincode)
#     return get_logincode
#
#
# class Case():
#     pass
#
#
# if __name__ == "__main__":
#     a = Case()
#
#     login_test(get_almightycode())
