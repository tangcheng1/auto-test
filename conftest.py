#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 15:06
# @Author  : tc
# @File    : conftest.py
# @Description :
import allure

from tools.base_requests import Utils
from tools.yaml_util import YamlUtil
import pytest
from tools.logger import logger


# conftest是测试前后的数据准备和处理
# 为了保证每个测试会话前extract.yaml列表数据是空的
@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtil().yaml_clear("data_yaml", "extract.yaml")
    yield
    YamlUtil().yaml_clear("data_yaml", "extract.yaml")


@pytest.fixture(scope="function", autouse=True)
def logger_test_print():
    logger.warning("---------------用例测试开始---------------\n")
    yield
    logger.warning("---------------用例测试结束---------------\n\n")


@pytest.fixture(scope="session", autouse=True)
def test_adminlogin():
    caseinfo = YamlUtil().yaml_read("data_yaml", "admin_login.yaml")[0]
    # 获取ymal
    value = caseinfo['request']
    # 读取extract.yaml文件，替换掉yaml中需要参数化的变量
    yaml_data = YamlUtil.extractdata_render_params(value)
    validate = value["validate"] if "validate" in value else None
    from tools.base_requests import Utils
    response = Utils.sendRequest(caseinfo['name'], yaml_data['method'], yaml_data['path'], yaml_data['params'],
                                 yaml_data['headers'])
    if "token" in str(response):
        YamlUtil().yaml_write({"amintoken": response["data"]["token"]}, "data_yaml", "extract.yaml")
    else:
        logger.info(f"token获取失败或者此为登录失败用例")
    if validate:
        Utils.validate(response, validate)


@pytest.fixture(scope="session", autouse=True)
def test_login():
    caseinfo_almighty_code = YamlUtil().yaml_read("data_yaml", "almighty_code.yaml")[0]
    value_almighty_code = caseinfo_almighty_code['request']
    response_almighty_code = Utils.sendRequest(caseinfo_almighty_code['name'], value_almighty_code['method'],
                                 value_almighty_code['path'], value_almighty_code['params'],
                                 value_almighty_code['headers'])
    YamlUtil().yaml_write({"smsCode": response_almighty_code["data"]}, "data_yaml", "extract.yaml")
    validate = value_almighty_code["validate"] if "validate" in value_almighty_code else None
    if validate:
        # logger.info(f"--预期验证的数据---\n{validate}")
        Utils.validate(response_almighty_code, validate)
    # 获取ymal
    caseinfo_rider_login = YamlUtil().yaml_read("data_yaml", "rider_login.yaml")[0]
    value = caseinfo_rider_login['request']
    # 更新需要参数化的万能验证码，完成接口关联
    # 读取extract.yaml文件，替换掉login.yaml中需要参数化的变量，这里是将万能验证码的值传入到验证码smsCode中
    yaml_data = YamlUtil.extractdata_render_params(value)
    validate = value["validate"] if "validate" in value else None
    response = Utils.sendRequest(caseinfo_rider_login['name'], yaml_data['method'], yaml_data['path'],
                                 yaml_data['params'], yaml_data['headers'])
    if "token" in str(response):
        YamlUtil().yaml_write({"token": response["data"]["token"]}, "data_yaml", "extract.yaml")
    else:
        logger.info(f"token获取失败或者此为登录失败用例")

    if validate:
        Utils.validate(response, validate)
