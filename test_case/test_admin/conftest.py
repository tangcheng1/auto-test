#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 15:06
# @Author  : tc
# @File    : conftest.py
# @Description :

from tools.yaml_util import YamlUtil
import pytest
from tools.logger import logger
from tools.base_requests import Utils
import allure
@allure.story('admin登录接口')
@pytest.fixture(scope="session", autouse=True)
def test_adminlogin():
    caseinfo=YamlUtil().yaml_read("data_yaml", "admin_login.yaml")[0]
    # 获取ymal
    value = caseinfo['request']
    # 读取extract.yaml文件，替换掉yaml中需要参数化的变量
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