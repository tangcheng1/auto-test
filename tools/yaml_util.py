#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 11:04
# @Author  : tc
# @File    : yaml_util.py
# @Description :
import yaml
from tools.logger import logger
from pathlib import Path

class YamlUtil:



    # def __init__(self,data,fileDir,yamlfileName):
    #
    #     self.fileDir  = fileDir
    #     self.yamlfileName = yamlfileName
    #     self.data = data

    # 读取yaml
    def yaml_read(self,yamlfileDir, yamlfileName):
        # 根据文件路径和名称获取数据
        work = f"{str(Path(__file__).parent.parent)}" + "/" + yamlfileDir + "/" + yamlfileName
        # logger.info("加载 {} 文件......".format(work))
        with open(work, encoding='utf-8', ) as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            # logger.info("读到数据 ==>>  {} ".format(value))
        return value

    # yaml的写入(data:写入内容，fileDir：文件路径，fileName：文件名字和后缀名)
    def yaml_write(self,data, fileDir, fileName):
        writework = f"{str(Path(__file__).parent.parent)}" + "/" + fileDir + "/" + fileName
        # logger.info("加载 {} 文件......".format(writework))
        with open(writework, encoding="utf-8", mode="a")as f:
            value = yaml.dump(data, stream=f, allow_unicode=True)
            # logger.info("写入数据 ==>>  {} ".format(value))
        return value

    # yaml的清除
    def yaml_clear(self, fileDir, fileName):
        writework = f"{str(Path(__file__).parent.parent)}" + "/" + fileDir + "/" + fileName
        with open(writework, mode='w', encoding='utf-8') as f:
            f.truncate()
