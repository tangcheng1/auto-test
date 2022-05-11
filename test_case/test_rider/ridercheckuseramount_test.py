#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/10 10:54
# @Author  : tc
# @File    : ridercheckuseramount_test.py
# @Description :

#
# import allure
# import pytest
# from tools.base_requests import Utils
# from tools.logger import logger
# from tools.yaml_util import YamlUtil
#
#
# class Testridercheckuseramount:
#     @allure.story('判断金额是否足够，同时计算出余额和优惠金额的扣除明细')
#     @pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "rider_check_user_amount.yaml"))
#     def test_ridercheckuseramount(self, caseinfo):
#         # 获取yaml的请求数据request
#         value = caseinfo['request']
#         # 更新yaml文件里面的带$值
#         extract = YamlUtil().yaml_read("data_yaml", "extract.yaml")
#         yaml_data = YamlUtil.extractdata_render_params(extract,value)
#         # files = value["files"] if "files" in test_case else None
#         # extract = value["extract"] if "extract" in value else None
#
#         validate = value["validate"] if "validate" in value else None
#         response = Utils.sendRequest(caseinfo['name'],yaml_data['method'], yaml_data['path'], yaml_data['params'], yaml_data['headers'])
#         # if "id" in str(response):
#         #     YamlUtil().yaml_write({"id": response["data"]["id"]}, "data_yaml", "extract.yaml")
#         if validate:
#             Utils.validate(response, validate)