#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 11:08
# @Author  : tc
# @File    : api_login.py
# @Description :
import json

import allure
import pytest
from tools.base_requests import Utils
from tools.logger import logger
from tools.yaml_util import YamlUtil


class Testlogin:
    @allure.story('骑手登录接口')
    @pytest.mark.dependency()
    @pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data", "login.yaml"))
    def test_login(self, caseinfo):
        # 获取ymal
        value = caseinfo['request']
        # 更新需要参数化的万能验证码，完成接口关联
        body = value['params']
        # for key, value in body.items():
        #     if key == value:
        #        value= YamlUtil().yaml_read("data", "extract.yaml")["almighty_code"]

        validate = value["validate"] if "validate" in value else None
        response = Utils.sendRequest(caseinfo['name'],value['method'], value['path'], body, value['headers'])
        if "token" == response.json():
            token = YamlUtil().yaml_write({"token": response["data"]["token"]}, "data", "extract.yaml")
        if validate:
            Utils.validate(response, validate)


if __name__ == '__main__':
    # Testwork().yaml_read()
    # Testwork().test_login()

    pytest.main(['-vs', 'login_test.py'])
