#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 11:04
# @Author  : tc
# @File    : yaml_util.py
# @Description :
import json
from string import Template

import yaml
from tools.logger import logger
from pathlib import Path


class YamlUtil:

    # 读取yaml
    @staticmethod
    def yaml_read(yamlfileDir, yamlfileName):
        # 根据文件路径和名称获取数据
        work = f"{str(Path(__file__).parent.parent)}" + "/" + yamlfileDir + "/" + yamlfileName
        # logger.info("加载 {} 文件......".format(work))
        with open(work, encoding='utf-8', ) as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            # logger.info("读到数据 ==>>  {} ".format(value))
        return value

    # yaml的写入(data_yaml:写入内容，fileDir：文件路径，fileName：文件名字和后缀名)
    @staticmethod
    def yaml_write(data, fileDir, fileName):
        writework = f"{str(Path(__file__).parent.parent)}" + "/" + fileDir + "/" + fileName
        # logger.info("加载 {} 文件......".format(writework))
        with open(writework, encoding="utf-8", mode="a")as f:
            value = yaml.dump(data, stream=f, allow_unicode=True)
            # logger.info("写入数据 ==>>  {} ".format(value))
        return value

    # yaml的清除
    @staticmethod
    def yaml_clear(fileDir, fileName):
        writework = f"{str(Path(__file__).parent.parent)}" + "/" + fileDir + "/" + fileName
        with open(writework, mode='w', encoding='utf-8') as f:
            f.truncate()

    # 用于替换yaml文件里的变量
    @staticmethod
    def extractdata_render_params(extractdata, casedata):
        # extractdata 是extract.yaml里存的变量
        # casedata 是请求的request
        extractdata = YamlUtil().yaml_read("data_yaml", "extract.yaml")
        tempTemplate1 = Template(str(casedata))
        c = tempTemplate1.safe_substitute(extractdata)
        yaml_data = yaml.safe_load(c)
        return yaml_data
