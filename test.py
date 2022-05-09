#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/9 11:39
# @Author  : tc
# @File    : test.py
# @Description :
from string import Template

import jsonpath
import pytest
import yaml

from tools.yaml_util import YamlUtil
from tools.logger import logger
from tools.yaml_util import YamlUtil


caseinfo = YamlUtil().yaml_read("data_yaml", "ridercheckusername.yaml")
value = caseinfo[0]['request']

extract = YamlUtil().yaml_read("data_yaml", "extract.yaml")
yaml_data = YamlUtil.extractdata_render_params(extract, value)
body = yaml_data

print(body)



