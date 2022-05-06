#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 11:08
# @Author  : tc
# @File    : api_login.py
# @Description :
import json

import allure
import pytest
import yaml
from config.config import *
import json
from tools.base_requests import assignment_yamlparams, sendRequest
from tools.logger import logger
from tools.yaml_util import YamlUtil


class Testwork():
    @allure.story('验证码接口')
    @allure.description("配置文件的组成：1、section：表示要标记的不同数据的区域 2、option：相当于字典当中的key 3、value：相当于字典当中的value")
    @pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data", "almightycode.yaml"))
    def test_almightycode(self, caseinfo):
        # 获取ymal
        value = assignment_yamlparams(caseinfo['request'])
        url = URL + value['path']
        response = sendRequest(value['method'], url, value['params'], value['headers'])
        almighty_code = YamlUtil().yaml_write({"almighty_code": response["data"]}, "data", "extract.yaml")
        assert response["code"] == "2"
        # return almighty_code

    @allure.story('骑手登录接口')
    @pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data", "login.yaml"))
    def test_login(self, caseinfo):
        # 获取ymal
        value = assignment_yamlparams(caseinfo['request'])
        # 更新需要参数化的万能验证码，完成接口关联
        value['params']['smsCode'] = YamlUtil().yaml_read("data", "extract.yaml")["almighty_code"]
        body= value['params']
        # value['params']['smsCode']= almighty_code
        # path = caseinfo['request']['path']
        # method = caseinfo['request']['method']
        # data = caseinfo['request']['params']
        # headers = caseinfo['request']['headers']
        # 拼接域名和path
        url = URL + value['path']
        response = sendRequest(value['method'], url ,body, value['headers'])
        assert response["code"] == "1"
        # print(response)


if __name__ == '__main__':
        # Testwork().yaml_read()
        # Testwork().test_login()

  pytest.main(['-vs', 'login_test.py'])
