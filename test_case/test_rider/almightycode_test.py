# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2022/5/6 18:28
# # @Author  : tc
# # @File    : almightycode_test.py
# # @Description :
# import allure
# import pytest
# import yaml
# from config.config import *
# import json
# from tools.base_requests import Utils
# from tools.logger import logger
# from tools.yaml_util import YamlUtil
#
#
# class Testwork():
#     params = YamlUtil().yaml_read("data_yaml", "almighty_code.yaml")
#     @allure.story(params[0])
#     @allure.description("配置文件的组成：1、section：表示要标记的不同数据的区域 2、option：相当于字典当中的key 3、value：相当于字典当中的value")
#     @pytest.mark.parametrize("caseinfo",params)
#     def test_almightycode(self, caseinfo):
#         value = caseinfo['request']
#         response = Utils.sendRequest(caseinfo['name'],value['method'], value['path'], value['params'], value['headers'])
#         YamlUtil().yaml_write({"smsCode": response["data"]}, "data_yaml", "extract.yaml")
#         # assert response["code"] == "1"
#         # print(response)
#         validate = value["validate"] if "validate" in value else None
#         if validate:
#             # logger.info(f"--预期验证的数据---\n{validate}")
#             Utils.validate(response, validate)
#
#
# if __name__ == '__main__':
#     pytest.main(['-vs', 'almightycode_test.py'])