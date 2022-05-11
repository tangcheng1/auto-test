#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 11:08
# @Author  : tc
# @File    : api_login.py
# @Description :
import json
from string import Template

import allure
import pytest
from tools.base_requests import Utils
from tools.logger import logger
from tools.yaml_util import YamlUtil
import yaml

class Testlogin:

    # params = YamlUtil().yaml_read("data_yaml", "almighty_code.yaml")
    # @allure.story(params[0]["name"])
    # @pytest.mark.parametrize("caseinfo",params)
    @allure.description("配置文件的组成：1、section：表示要标记的不同数据的区域 2、option：相当于字典当中的key 3、value：相当于字典当中的value")
    @pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "almighty_code.yaml"))
    def test_almightycode(self,caseinfo):
        value = caseinfo['request']
        response = Utils.sendRequest(caseinfo['name'], value['method'], value['path'], value['params'],value['headers'])
        YamlUtil().yaml_write({"smsCode": response["data"]}, "data_yaml", "extract.yaml")
        validate = value["validate"] if "validate" in value else None
        if validate:
            # logger.info(f"--预期验证的数据---\n{validate}")
            Utils.validate(response, validate)

    @allure.story('骑手登录接口')
    # @pytest.mark.dependency(depends=['Testlogin::test_almightycode'])
    @pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "rider_login.yaml"))
    def test_login(self,caseinfo):
        # 获取ymal
        value = caseinfo['request']
        # 更新需要参数化的万能验证码，完成接口关联
        # 读取extract.yaml文件，替换掉login.yaml中需要参数化的变量，这里是将万能验证码的值传入到验证码smsCode中
        extract = YamlUtil().yaml_read("data_yaml", "extract.yaml")
        yaml_data = YamlUtil.extractdata_render_params(extract,value)
        validate = value["validate"] if "validate" in value else None
        response = Utils.sendRequest(caseinfo['name'],yaml_data['method'], yaml_data['path'], yaml_data['params'], yaml_data['headers'])
        if "token" in str(response):
            YamlUtil().yaml_write({"token":response["data"]["token"]}, "data_yaml", "extract.yaml")
        else:
            logger.info(f"token获取失败或者此为登录失败用例")

        if validate:
            Utils.validate(response, validate)


if __name__ == '__main__':
    # Testwork().yaml_read()
    # Testwork().test_login()

    pytest.main(['-vs', 'login_test.py'])
