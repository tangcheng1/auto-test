# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/11 14:53
# @Author  : tc
# @File    : admin_wallet_add_test.py
# @Description :
from decimal import Decimal

import allure
import pytest
import yaml
import json
from tools.base_requests import Utils
from tools.calculation_function import actualamt, couponAmt, totalChangeAmt
from tools.logger import logger
from tools.yaml_util import YamlUtil
from tools.random_function import random_name, random_phone
import pytest_check as check

random_name_new = random_name()
random_phone_new = random_phone()


# WalletUserName = YamlUtil().yaml_read("config", "config.yaml")['WalletUserName']
#
# print(WalletUserName)
# print(type(WalletUserName))


# @allure.story('admin登录接口')
# @pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "admin_login.yaml"))
# def test_adminlogin(caseinfo):
#     # 获取ymal
#     value = caseinfo['request']
#     # 读取extract.yaml文件，替换掉yaml中需要参数化的变量
#     yaml_data = YamlUtil.extractdata_render_params(value)
#     validate = value["validate"] if "validate" in value else None
#     response = Utils.sendRequest(caseinfo['name'], yaml_data['method'], yaml_data['path'], yaml_data['params'],
#                                  yaml_data['headers'])
#     if "token" in str(response):
#         YamlUtil().yaml_write({"amintoken": response["data"]["token"]}, "data_yaml", "extract.yaml")
#     else:
#         logger.info(f"token获取失败或者此为登录失败用例")
#     if validate:
#         Utils.validate(response, validate)
@allure.story('admin新增客户')
@pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "admin_wallet_add.yaml"))
def test_admin_wallet_add(caseinfo):
    # 获取ymal
    value = caseinfo['request']
    # 主动替换yaml中想要替换的变量,key为带$后面的名称，value为想替换的数据
    list = [{'updatenickName': random_name_new}, {'PhoneMain': random_phone_new}, {'actualAmt': actualamt},
            {'couponAmt': couponAmt}]
    for i in list:
        pr = YamlUtil.data_update_params(value, i)
        value = pr
    # 读取extract.yaml文件，替换掉yaml中需要参数化的变量，
    yaml_data = YamlUtil.extractdata_render_params(value)
    YamlUtil().yaml_write(list[1], "data_yaml", "extract.yaml")
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
    # 先判断该用户在不在返回的结果中
    if str(random_phone_new) in str(response):
        # 在列表中，循环获得该用户信息断言
        reslist = response['list']
        for i in reslist:
            if i['userName'] == str(random_phone_new):
                check.equal(Decimal(str(i['actualAmt'])), actualamt, "充值金额断言")
                check.equal(Decimal(str(i['couponAmt'])), couponAmt, "优惠金额断言")
                check.equal(i['userName'], str(random_phone_new), "手机号断言")
                check.equal(i['nickName'], str(random_name_new), "用户昵称断言")
                YamlUtil().yaml_write({"id_wallet_list": i['id']}, "data_yaml", "extract.yaml")

    else:
        check.is_in(str(random_phone_new), str(response), "未找到{}该用户的信息".format(str(random_phone_new)))
        # logger.info("未找到{}该用户的信息".format(str(WalletUserName)))

    if validate:
        Utils.validate(response, validate)


@allure.story('admin充值记录')
@pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "admin_wallet_log_list.yaml"))
def test_admin_wallet_log_list(caseinfo):
    # 获取ymal
    value = caseinfo['request']
    yaml_data = YamlUtil.extractdata_render_params(value)
    validate = value["validate"] if "validate" in value else None
    response = Utils.sendRequest(caseinfo['name'], yaml_data['method'], yaml_data['path'], yaml_data['params'],
                                 yaml_data['headers'])
    # 先判断该用户在不在返回的结果中
    if str(random_phone_new) in str(response):
        # 在列表中，循环获得该用户信息断言
        reslist = response['list']
        for i in reslist:
            if i['userName'] == str(random_phone_new):
                check.equal(Decimal(str(i['actualAmt'])), actualamt, "充值金额断言")
                check.equal(Decimal(str(i['couponAmt'])), couponAmt, "优惠金额断言")
                check.equal(i['userName'], str(random_phone_new), "手机号断言")
                check.equal(Decimal(str(i['totalChangeAmt'])), totalChangeAmt, "充值总金额（充值的金额+优惠金额）断言")
                check.equal(Decimal(str(i['remainActualAmt'])), actualamt, "剩余充值总额断言")
                check.equal(Decimal(str(i['remainCouponAmt'])), couponAmt, "剩余优惠总额断言")

    else:
        check.is_in(str(random_phone_new), str(response), "未找到{}该用户的信息".format(str(random_phone_new)))
        # logger.info("未找到{}该用户的信息".format(str(WalletUserName)))

    if validate:
        Utils.validate(response, validate)


@allure.story('admin修改客户姓名和备注')
@pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "admin_wallet_edit.yaml"))
def test_admin_wallet_edit(caseinfo):
    # 获取ymal
    value = caseinfo['request']
    random_name_edit = random_name()
    # 主动替换yaml中想要替换的变量,key为带$后面的名称，value为想替换的数据
    list = [{'updatenickName': random_name_edit}]
    for i in list:
        pr = YamlUtil.data_update_params(value, i)
        value = pr
    yaml_data = YamlUtil.extractdata_render_params(value)
    validate = value["validate"] if "validate" in value else None
    response_edit = Utils.sendRequest(caseinfo['name'], yaml_data['method'], yaml_data['path'], yaml_data['params'],
                                      yaml_data['headers'])

    if validate:
        Utils.validate(response_edit, validate)

    '''    
    客户列表校验下一修改后的内容正确
    '''
    admin_wallet_list = YamlUtil().yaml_read("data_yaml", "admin_wallet_list.yaml")[0]
    value = admin_wallet_list['request']
    yaml_data_list = YamlUtil.extractdata_render_params(value)
    response = Utils.sendRequest(admin_wallet_list['name'], yaml_data_list['method'], yaml_data_list['path'],
                                 yaml_data_list['params'],
                                 yaml_data_list['headers'])
    # 先判断该用户在不在返回的结果中
    if str(random_phone_new) in str(response):
        # 在列表中，循环获得该用户信息断言
        reslist = response['list']
        for i in reslist:
            if i['userName'] == str(random_phone_new):
                check.equal(Decimal(str(i['actualAmt'])), actualamt, "充值金额断言")
                check.equal(Decimal(str(i['couponAmt'])), couponAmt, "优惠金额断言")
                check.equal(i['userName'], str(random_phone_new), "手机号断言")
                check.equal(i['nickName'], str(random_name_edit), "用户昵称断言")
                check.equal(i['remark'], 'fffffffffff', "备注断言")
                # YamlUtil().yaml_write({"id_wallet_list":i['id']}, "data_yaml", "extract.yaml")

    else:
        check.is_in(str(random_phone_new), str(response), "未找到{}该用户的信息".format(str(random_phone_new)))
        # logger.info("未找到{}该用户的信息".format(str(WalletUserName)))

    if validate:
        Utils.validate(response, validate)


@allure.story('admin充值接口')
@pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "admin_wallet_recharge.yaml"))
def test_admin_wallet_recharge(caseinfo):
    # 获取ymal
    value = caseinfo['request']
    # 主动替换yaml中想要替换的变量,key为带$后面的名称，value为想替换的数据
    list = [{'PhoneMain': random_phone_new}]
    for i in list:
        pr = YamlUtil.data_update_params(value, i)
        value = pr
    yaml_data = YamlUtil.extractdata_render_params(value)
    validate = value["validate"] if "validate" in value else None
    response_edit = Utils.sendRequest(caseinfo['name'], yaml_data['method'], yaml_data['path'], yaml_data['params'],
                                      yaml_data['headers'])

    if validate:
        Utils.validate(response_edit, validate)

    '''    
    客户列表校验下一充值后的内容正确
    '''
    admin_wallet_list = YamlUtil().yaml_read("data_yaml", "admin_wallet_list.yaml")[0]
    value = admin_wallet_list['request']
    yaml_data_list = YamlUtil.extractdata_render_params(value)
    response = Utils.sendRequest(admin_wallet_list['name'], yaml_data_list['method'], yaml_data_list['path'],
                                 yaml_data_list['params'],
                                 yaml_data_list['headers'])
    # 先判断该用户在不在返回的结果中
    if str(random_phone_new) in str(response):
        # 在列表中，循环获得该用户信息断言
        reslist = response['list']
        for i in reslist:
            if i['userName'] == str(random_phone_new):
                check.equal(Decimal(str(i['actualAmt'])), actualamt + 10, "充值金额断言")
                check.equal(Decimal(str(i['couponAmt'])), couponAmt, "优惠金额断言")
                check.equal(i['userName'], str(random_phone_new), "手机号断言")
                check.equal(i['remark'], 'fffffffffff', "备注断言")
                # YamlUtil().yaml_write({"id_wallet_list":i['id']}, "data_yaml", "extract.yaml")

    else:
        check.is_in(str(random_phone_new), str(response), "未找到{}该用户的信息".format(str(random_phone_new)))
        # logger.info("未找到{}该用户的信息".format(str(WalletUserName)))

    if validate:
        Utils.validate(response, validate)

    '''    
    充值记录验下一充值后的内容正确
    '''
    admin_wallet_log_list = YamlUtil().yaml_read("data_yaml", "admin_wallet_log_list.yaml")[0]
    yaml_data_log_list = YamlUtil.extractdata_render_params(admin_wallet_log_list['request'])
    validate = value["validate"] if "validate" in value else None
    response_log_list = Utils.sendRequest(admin_wallet_log_list['name'], yaml_data_log_list['method'],
                                          yaml_data_log_list['path'], yaml_data_log_list['params'],
                                          yaml_data_log_list['headers'])
    # 先判断该用户在不在返回的结果中
    if str(random_phone_new) in str(response_log_list):
        # 在列表中，循环获得该用户信息断言
        reslist = response_log_list['list']
        i = reslist[0]
        check.equal(Decimal(str(i['actualAmt'])), Decimal(10), "充值金额断言")
        check.equal(i['couponAmt'], Decimal(0), "优惠金额断言")
        check.equal(i['userName'], str(random_phone_new), "手机号断言")
        check.equal(Decimal(str(i['totalChangeAmt'])), Decimal(10), "充值总金额（充值的金额+优惠金额）断言")
        check.equal(Decimal(str(i['remainActualAmt'])), Decimal(actualamt) + 10, "剩余充值总额断言")
        check.equal(Decimal(str(i['remainCouponAmt'])), Decimal(couponAmt), "剩余优惠总额断言")

    else:
        check.is_in(str(random_phone_new), str(response), "未找到{}该用户的信息".format(str(random_phone_new)))
        # logger.info("未找到{}该用户的信息".format(str(WalletUserName)))

    if validate:
        Utils.validate(response, validate)


if __name__ == '__main__':
    pytest.main(['-vs', 'admin_wallet_list_test.py'])
