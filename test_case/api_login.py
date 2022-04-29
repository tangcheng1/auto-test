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
import json
from tools.base_requests import yaml_read, sendRequest, assignment_yamlparams
from pathlib import Path


class Testwork():



    cls.almightycode = None


    @pytest.mark.parametrize("caseinfo", yaml_read("data", "almightycode.yaml"))
    def test_almightycode(self, caseinfo):
        # 获取ymal
        value = assignment_yamlparams(caseinfo['request'])
        url = URL + value['path']
        response = sendRequest(value['method'], url, value['headers'], value['params'])
        print(response["data"])
        return response["data"]


    @pytest.mark.parametrize("caseinfo", yaml_read("data", "login.yaml"))
    def test_login(self, caseinfo):
        # 获取ymal
        value = assignment_yamlparams(caseinfo['request'])
        # path = caseinfo['request']['path']
        # method = caseinfo['request']['method']
        # data = caseinfo['request']['params']
        # headers = caseinfo['request']['headers']
        # 拼接域名和path
        url = URL + value['path']
        response = sendRequest(value['method'], url, value['headers'], value['params'])
        print(response)


if __name__ == '__main__':
    # Testwork().yaml_read()
    # Testwork().test_login()

    pytest.main(['-vs', 'api_login.py'])
