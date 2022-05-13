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
from tools.calculation_function import actualamt, couponAmt
from tools.logger import logger
from tools.yaml_util import YamlUtil
from tools.random_function import random_name, random_phone
import pytest_check as check



random_name_new = random_name()
random_phone_new = random_phone()
WalletUserName = YamlUtil().yaml_read("config", "config.yaml")['WalletUserName']

print(WalletUserName)
print(type(WalletUserName))
@allure.story('admin登录接口')
@pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "admin_login.yaml"))
def test_adminlogin(caseinfo):
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


@allure.story('admin新增客户')
@pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "admin_wallet_add.yaml"))
def test_admin_wallet_add(caseinfo):
    # 获取ymal
    value = caseinfo['request']
    # 主动替换yaml中想要替换的变量,key为带$后面的名称，value为想替换的数据
    list = [{'updatenickName': random_name_new}, {'PhoneMain': random_phone_new},{'actualAmt':actualamt}, {'couponAmt':couponAmt}]
    for i in list:
        pr = YamlUtil.data_update_params(value, i)
        value = pr
    # 读取extract.yaml文件，替换掉yaml中需要参数化的变量，
    yaml_data = YamlUtil.extractdata_render_params(value)
    validate = value["validate"] if "validate" in value else None
    response = Utils.sendRequest(caseinfo['name'], yaml_data['method'], yaml_data['path'], yaml_data['params'],
                                 yaml_data['headers'])
    if validate:
        Utils.validate(response, validate)

@allure.story('admin客户钱包列表')
@pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "admin_wallet_list.yaml"))
def test_admin_wallet_list(caseinfo):
    # 获取ymal
    value = caseinfo['request']
    yaml_data = YamlUtil.extractdata_render_params(value)
    validate = value["validate"] if "validate" in value else None
    response = Utils.sendRequest(caseinfo['name'], yaml_data['method'], yaml_data['path'], yaml_data['params'],
                                 yaml_data['headers'])
    # 先判断该用户在不在结果中
    if str(random_phone_new) in str(response):
        # 在列表中，循环获得该用户信息断言
        reslist = response['list']
        for i in reslist:
            if i['userName'] == str(random_phone_new):
                check.equal(i['actualAmt'],float(actualamt),"充值金额断言")
                check.equal(i['couponAmt'],float(couponAmt),"优惠金额断言")
                check.equal(i['userName'], str(random_phone_new),"手机号断言")
                check.equal(i['nickName'], str(random_name_new),"用户昵称断言")
                # logger.info("充值金额{}".format(actualAmt))
    else:
        check.is_in(str(random_phone_new), str(response),"未找到{}该用户的信息".format(str(random_phone_new)))
        # logger.info("未找到{}该用户的信息".format(str(WalletUserName)))

    if validate:
        Utils.validate(response, validate)

if __name__ == '__main__':
    pytest.main(['-vs', 'admin_wallet_list_test.py'])
