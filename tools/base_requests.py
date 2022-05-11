import json, os
from string import Template

from tools.logger import logger
import xlrd
from requests import request
from tools.yaml_util import YamlUtil
import requests
import jsonpath
import allure

class Utils:


    @staticmethod
    # 重写post 和get请求，方便自动去请求
    def sendRequest(name, method, url, data, headers, **kwargs):
        # 把请求方法改成小写
        method = str(method).lower()
        rep = None
        # 用请求路径和域名拼接成完成的请求链接
        URL = YamlUtil.yaml_read("config", "config.yaml")['server']['api']
        url = URL + url
        # get请求以params接参数
        if method == "get":
            rep = request(method=method, url=url, params=data, headers=headers, **kwargs)
        # post请求以data接参数,原因：data只能传输简单的只有键值对的dict或者str格式的数据，json一般只能传输dict格式，简单复杂的都可以
        # data可以满足多种格式，那我们只需把都转成str类型
        elif method == "post":
            # 把键值对转换成str类型
            data = json.dumps(data)
            rep = request(method=method, url=url, data=data, headers=headers, **kwargs)
        # 打印请求前日志
        logger.info("---------------接口测试开始---------------")
        Utils.request_log(name, method, url, data, headers)
        logger.info("实际结果:{}".format(rep.json()))
        return rep.json()

    # 断言方法
    @staticmethod
    def validate(response, validate: list):
        for val in validate:
            for key, item in val.items():
                for key_json_path, item_expect in item.items():
                    item_expect = str(item_expect)
                    logger.info(f"预期结果的值是{item_expect}")
                    actual_val = jsonpath.jsonpath(response, key_json_path)[0]
                    logger.info(f"获取真实值是{actual_val}")
                    if key == "equal_to":
                        assert actual_val == item_expect
                    else:
                        logger.info("-------暂时不支持该断言方法---------")
        logger.info("---------------接口测试结束---------------")

    @staticmethod
    def request_log(name, method, url, data=None, headers=None, files=None, cookies=None, **kwargs):
        logger.info("接口名称:{}".format(name))
        logger.info("请求地址:{}".format(url))
        logger.info("请求方式:{}".format(method))
        logger.info("请求body:{}".format(json.dumps(data, indent=4, ensure_ascii=False)))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        logger.info("请求头{}".format(headers, indent=4, ensure_ascii=False))
        # logger.info("接口请求 params 参数 ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        #
        #
        # logger.info("接口上传附件 files 参数 ==>> {}".format(files))
        # logger.info("接口 cookies 参数 ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))

        # (method=method, url=url, data_yaml=data_yaml, headers=headers, ** kwargs)

    # @staticmethod
    # def extract(response, extract: dict):
    #     for key, val in extract.items():
    #         set_value = jsonpath.jsonpath(response, val)[0]
    #         logger.info(f"提取的值是{set_value}")
    #         # setattr(EnvData, key, str(set_value))
    #
    #
    # # 自动分配yaml参数
    # @staticmethod
    # def assignment_yamlparams(kwargs):
    #     for key, value in kwargs.items():
    #         if type(value) is dict:
    #             kwargs.assignment_yamlparams(value)
    #         else:
    #             if value:
    #                 pass
    #             else:
    #                 kwargs[key] = getattr(key)
    #     return kwargs
    # 读取excel
    # @staticmethod
    # def excel_read():
    #     book = xlrd.open_workbook("../data_yaml/case_data1.xls")
    #     # 读取第一个sheet页
    #     sheet = book.sheet_by_index(0)
    #     list = []
    #     for norw in range(1, sheet.nrows):
    #         # if sheet.cell_value(norw, 4) != "否":  # 每行第4列等于否将不读取内容
    #
    #         dict_case = dict(
    #             url=sheet.cell_value(norw, 3),
    #             headers=sheet.cell_value(norw, 2),
    #             method=sheet.cell_value(norw, 5),
    #             data=sheet.cell_value(norw, 8))
    #         list.append(dict_case)
    #         # value = table.row_values(norw)
    #         # value = table.col_values(norw)
    #         # value.pop(4)   #删除是否的那一列
    #     # print(list)
    #     return list
if __name__ == '__main__':
    work = YamlUtil().yaml_read("data_yaml", "rider_login.yaml")
    # work =f"{str(Path(__file__).parent.parent)}/data_yaml/rider_login.yaml"
    print(work)
