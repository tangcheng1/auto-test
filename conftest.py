#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 15:06
# @Author  : tc
# @File    : conftest.py
# @Description :
import pytest

from tools.logger import logger
from tools.yaml_util import YamlUtil




@pytest.fixture(scope="session",autouse=True)
def clear_yaml():
    YamlUtil().yaml_clear("data","extract.yaml")