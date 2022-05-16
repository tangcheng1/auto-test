#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/16 11:07
# @Author  : tc
# @File    : admin_rider_add_test.py
# @Description :
import allure
import pytest
import yaml
import json
from tools.base_requests import Utils
from tools.calculation_function import actualamt, couponAmt,totalChangeAmt
from tools.logger import logger
from tools.yaml_util import YamlUtil
from tools.random_function import random_name, random_phone
import pytest_check as check

random_name_new = random_name()
random_phone_new = random_phone()

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


@allure.story('admin新增骑手')
@pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "admin_rider_add.yaml"))
def test_admin_rider_add(caseinfo):
    # 获取ymal
    value = caseinfo['request']

    # 主动替换yaml中想要替换的变量,key为带$后面的名称，value为想替换的数据
    list = [{'updatenickName': random_name_new}, {'PhoneMain': random_phone_new}]
    for i in list:
        pr = YamlUtil.data_update_params(value, i)
        value = pr
    yaml_data = YamlUtil.extractdata_render_params(value)
    validate = value["validate"] if "validate" in value else None
    response_edit = Utils.sendRequest(caseinfo['name'], yaml_data['method'], yaml_data['path'], yaml_data['params'],
                                 yaml_data['headers'])

    if validate:
        Utils.validate(response_edit, validate)

@allure.story('admin骑手列表')
@pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "admin_rider_list.yaml"))
def test_admin_rider_list(caseinfo):
    # 获取ymal
    value = caseinfo['request']
    # 主动替换yaml中想要替换的变量,key为带$后面的名称，value为想替换的数据
    list = [{'updatenickName': random_name_new}, {'PhoneMain': random_phone_new}]
    for i in list:
        pr = YamlUtil.data_update_params(value, i)
        value = pr
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
                check.equal(i['userName'], str(random_phone_new), "手机号断言")
                check.equal(i['nickName'], str(random_name_new), "昵称断言")
                check.equal(i['idCardCode'], str(random_phone_new), "身份证断言")
                YamlUtil().yaml_write({"id_rider_list":i['id']}, "data_yaml", "extract.yaml")

    else:
        check.is_in(str(random_phone_new), str(response), "未找到{}该用户的信息".format(str(random_phone_new)))
        # logger.info("未找到{}该用户的信息".format(str(WalletUserName)))
    if validate:
        Utils.validate(response, validate)

@allure.story('admin骑手信息编辑')
@pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "admin_rider_update.yaml"))
def test_admin_rider_update(caseinfo):
    # 获取ymal
    value = caseinfo['request']
    # 主动替换yaml中想要替换的变量,key为带$后面的名称，value为想替换的数据
    random_name_update = random_name()
    random_phone_update = random_phone()
    list = [{'PhoneMain': random_phone_new},{'idCardCode': random_phone_update},{'updatenickName': random_name_update}]
    for i in list:
        pr = YamlUtil.data_update_params(value, i)
        value = pr
    yaml_data = YamlUtil.extractdata_render_params(value)
    validate = value["validate"] if "validate" in value else None
    response_update = Utils.sendRequest(caseinfo['name'], yaml_data['method'], yaml_data['path'], yaml_data['params'],
                                 yaml_data['headers'])

    if validate:
        Utils.validate(response_update, validate)
    '''    
    骑手列表校验下一充值后的内容正确
    '''
    admin_rider_list = YamlUtil().yaml_read("data_yaml", "admin_rider_list.yaml")[0]
    value = admin_rider_list['request']
    yaml_data_list = YamlUtil.extractdata_render_params(value)
    response = Utils.sendRequest(admin_rider_list['name'], yaml_data_list['method'], yaml_data_list['path'],
                                 yaml_data_list['params'],
                                 yaml_data_list['headers'])
    # 先判断该用户在不在返回的结果中
    if str(random_phone_new) in str(response):
        # 在列表中，循环获得该用户信息断言
        reslist = response['list']
        for i in reslist:
            if i['userName'] == str(random_phone_new):
                check.equal(i['userName'], str(random_phone_new), "手机号断言")
                check.equal(i['nickName'], str(random_name_update), "昵称断言")
                check.equal(i['idCardCode'], str(random_phone_update), "身份证断言")

    else:
        check.is_in(str(random_phone_new), str(response), "未找到{}该用户的信息".format(str(random_phone_new)))
        # logger.info("未找到{}该用户的信息".format(str(WalletUserName)))
    if validate:
        Utils.validate(response, validate)

@allure.story('admin删除骑手')
@pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "admin_rider_delete.yaml"))
def test_admin_rider_delete(caseinfo):
    # 获取ymal
    value = caseinfo['request']
    yaml_data = YamlUtil.extractdata_render_params(value)
    validate = value["validate"] if "validate" in value else None
    response_update = Utils.sendRequest(caseinfo['name'], yaml_data['method'], yaml_data['path'], yaml_data['params'],
                                 yaml_data['headers'])

    if validate:
        Utils.validate(response_update, validate)
    '''    
    骑手列表校验下一充值后的内容正确
    '''
    admin_rider_list = YamlUtil().yaml_read("data_yaml", "admin_rider_list.yaml")[0]
    value = admin_rider_list['request']
    yaml_data_list = YamlUtil.extractdata_render_params(value)
    response = Utils.sendRequest(admin_rider_list['name'], yaml_data_list['method'], yaml_data_list['path'],
                                 yaml_data_list['params'],
                                 yaml_data_list['headers'])

    check.is_not_in(str(random_phone_new), str(response),"用户删除成功")
        # logger.info("未找到{}该用户的信息".format(str(WalletUserName)))
    if validate:
        Utils.validate(response, validate)


if __name__ == '__main__':
    pytest.main(['-vs', 'admin_rider_add_test.py'])