#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 11:08
# @Author  : tc
# @File    : api_login.py
# @Description :
import json
import pytest
import requests
import yaml
from config.config import *
from tools.base_requests import yaml_read, sendRequest




class Testwork():






    @pytest.mark.parametrize("caseinfo", yaml_read())
    def test_login(self, caseinfo):
        path = caseinfo['request']['path']
        method = caseinfo['request']['method']
        data = caseinfo['request']['params']
        headers = caseinfo['request']['headers']
        url = URL + path
        response = sendRequest(method,url,headers,data)
        print(response)



if __name__ == '__main__':
    # Testwork().yaml_read()
    # Testwork().test_login()

    pytest.main(['-vs', 'api_login.py'])
