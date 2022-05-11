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
    YamlUtil().yaml_clear("data_yaml", "extract.yaml")
    yield
    YamlUtil().yaml_clear("data_yaml", "extract.yaml")
