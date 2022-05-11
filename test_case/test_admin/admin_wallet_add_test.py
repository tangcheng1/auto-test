# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/11 14:53
# @Author  : tc
# @File    : admin_wallet_add_test.py
# @Description :

import allure
import pytest
import yaml
import json
from tools.base_requests import Utils
from tools.logger import logger
from tools.yaml_util import YamlUtil
from tools.random_function import random_name

@allure.story('admin登录接口')
@pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "admin_login.yaml"))
def test_adminlogin(caseinfo):
    # 获取ymal
    value = caseinfo['request']
    # 更新需要参数化的万能验证码，完成接口关联
    # 读取extract.yaml文件，替换掉login.yaml中需要参数化的变量，这里是将万能验证码的值传入到验证码smsCode中
    yaml_data = YamlUtil.extractdata_render_params(value)
    validate = value["validate"] if "validate" in value else None
    response = Utils.sendRequest(caseinfo['name'], yaml_data['method'], yaml_data['path'], yaml_data['params'],
                                 yaml_data['headers'])
    if "token" in str(response):
        YamlUtil().yaml_write({"amintoken": response["data"]["token"]}, "data_yaml", "extract.yaml")
    else:
        logger.info(f"token获取失败或者此为登录失败用例")
    if validate:
        Utils.validate(response, validate)

@allure.story('admin新增客户')
@pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "admin_wallet_add.yaml"))
def test_admin_wallet_add(caseinfo):
    # 获取ymal
    value = caseinfo['request']
    # 更新需要参数化的万能验证码，完成接口关联
    # 读取extract.yaml文件，替换掉login.yaml中需要参数化的变量，这里是将万能验证码的值传入到验证码smsCode中
    body=YamlUtil.data_update_params(value,"updatenickName",random_name())
    yaml_data = YamlUtil.extractdata_render_params(body)
    validate = value["validate"] if "validate" in value else None
    response = Utils.sendRequest(caseinfo['name'], yaml_data['method'], yaml_data['path'], yaml_data['params'],
                                 yaml_data['headers'])
    if validate:
        Utils.validate(response, validate)
if __name__ == '__main__':
    pytest.main(['-vs', 'adminlogin.py'])