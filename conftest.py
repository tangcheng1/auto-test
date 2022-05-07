#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 15:06
# @Author  : tc
# @File    : conftest.py
# @Description :

from tools.yaml_util import YamlUtil
import pytest
from tools.logger import logger

# conftest是测试前后的数据准备和处理


# 为了保证每个测试会话前extract.yaml列表数据是空的
@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtil().yaml_clear("data", "extract.yaml")

# def pytest_collect_file(parent, path):
#     # 获取文件.yml 文件,匹配规则
#     if path.ext == ".yml" and path.basename.startswith("test"):
#         print(path)
#         print(parent)
#         return YamlFile(path, parent)
#
#
# class YamlFile(pytest.File):
#     '''收集测试用例'''
#     def collect(self):
#         yml_raw = self.fspath.open(encoding='utf-8').read()
#         yml_var = Template(yml_raw).safe_substitute(os.environ)
#         yaml_data = yaml.safe_load(yml_var)
#         for yaml_case in yaml_data:
#             name = yaml_case.get("test").get("name")
#             values = yaml_case.get("test")
#             yield YamlTest(name, self, values)
#
#
# class YamlTest(pytest.Item):
#     def __init__(self, name, parent, values):
#         super(YamlTest, self).__init__(name, parent)
#         self.name = name
#         self.values = values
#         self.s = requests.session()
#
#     def values_render_variable(self, values):
#         # values 是Test用例部分
#         yaml_test = Template(json.dumps(values)).safe_substitute(os.environ)
#         values = yaml.safe_load(yaml_test)
#         return values
#
#     def runtest(self):
#         # 运行用例
#         values = self.values_render_variable(self.values)
#         request_data = values.get("request")
#         print("\n请求数据: ", request_data)
#         print(request_data)
#         response = self.s.request(**request_data)
#         print("接口返回", response.text)
#         # 判断是否有extract提取参数
#         if values.get("extract"):
#             for key, value in values.get("extract").items():
#                 os.environ[key] = jsonpath.jsonpath(response.json(), value)[0]
#         self.assert_response(response, values.get("validate"))
#
#     def assert_response(self, response, validate):
#         '''设置断言'''
#         if validate:
#             for i in validate:
#                 if "eq" in i.keys():
#                     yaml_result = i.get("eq")[0]
#                     actual_result = jsonpath.jsonpath(response.json(), yaml_result)
#                     expect_result = i.get("eq")[1]
#                     print("实际结果：%s" % actual_result[0])
#                     print("期望结果：%s" % expect_result)
#                     assert actual_result[0] == expect_result
