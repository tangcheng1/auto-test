#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/7 09:53
# @Author  : tc
# @File    : ridercheckusername_test.py
# @Description :

import allure
import pytest
from tools.base_requests import Utils
from tools.logger import logger
from tools.yaml_util import YamlUtil


class Testridercheckusername:
    @allure.story('检查用户手机号，查询用户昵称信息')
    @pytest.mark.parametrize("caseinfo", YamlUtil().yaml_read("data_yaml", "ridercheckusername.yaml"))
    def test_login(self, caseinfo):
        # 获取ymal的请求数据request
        value = caseinfo['request']
        # 更新yaml文件里面的带$值
        extract = YamlUtil().yaml_read("data_yaml", "extract.yaml")
        yaml_data = YamlUtil.extractdata_render_params(extract,value)
        # files = value["files"] if "files" in test_case else None
        # extract = value["extract"] if "extract" in value else None
        validate = value["validate"] if "validate" in value else None
        response = Utils.sendRequest(caseinfo['name'],yaml_data['method'], yaml_data['path'], yaml_data['params'], yaml_data['headers'])
        if validate:
            Utils.validate(response, validate)