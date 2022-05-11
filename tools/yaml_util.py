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

        return value

    # yaml的清除
    @staticmethod
    def yaml_clear(fileDir, fileName):
        writework = f"{str(Path(__file__).parent.parent)}" + "/" + fileDir + "/" + fileName
        with open(writework, mode='w', encoding='utf-8') as f:
            f.truncate()

    # 用于从extract.yaml中替换yaml文件里的变量
    @staticmethod
    def extractdata_render_params(casedata):
        # extractdata 是extract.yaml里存的变量
        # casedata 是请求的request
        # 先获得config里面的配置数据
        config = YamlUtil().yaml_read("config", "config.yaml")
        tempTemplate1 = Template(str(casedata))    #原数据的来源
        c1 = tempTemplate1.safe_substitute(config)  #替换数据的来源
        yaml_config_data = yaml.safe_load(c1)
        # 在获取extract.yaml里存的变量
        extractdata = YamlUtil().yaml_read("data_yaml", "extract.yaml")
        tempTemplate1 = Template(str(yaml_config_data))     #原数据的来源
        c2 = tempTemplate1.safe_substitute(extractdata)  #替换数据的来源
        yaml_data = yaml.safe_load(c2)
        logger.info("替换后的yaml文件{} ".format(yaml_data))
        return yaml_data

    # 替换数据： casedata：来源数据，json格式；value：带$的名称；valueupdate：替换后的数据
    @staticmethod
    def data_update_params(casedata,value,valueupdate):
        tempTemplate1 = Template(str(casedata))  # 原数据的来源
        c1 = tempTemplate1.safe_substitute({value:valueupdate}) # 替换数据的来源
        update_params = yaml.safe_load(c1)
        return update_params