import json
import os

import xlrd
import yaml
from requests import request
from pathlib import Path


# 读取excel
def excel_read():
    book = xlrd.open_workbook("../data/case_data1.xls")
    # 读取第一个sheet页
    sheet = book.sheet_by_index(0)
    list = []
    for norw in range(1, sheet.nrows):
        # if sheet.cell_value(norw, 4) != "否":  # 每行第4列等于否将不读取内容

        dict_case = dict(
            url=sheet.cell_value(norw, 3),
            headers=sheet.cell_value(norw, 2),
            method=sheet.cell_value(norw, 5),
            data=sheet.cell_value(norw, 8))
        list.append(dict_case)
        # value = table.row_values(norw)
        # value = table.col_values(norw)
        # value.pop(4)   #删除是否的那一列
    # print(list)
    return list


# 读取yaml
def yaml_read(yamlfileDir, yamlfileName):
    # 根据文件路径和名称获取数据
    work = f"{str(Path(__file__).parent.parent)}" + "/" + yamlfileDir + "/" + yamlfileName
    # print(work)
    with open(work, encoding='utf-8', ) as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        # print(value["request"])
    return value


# yaml的写入
def yaml_write(data, fileDir, fileName):
    writework = f"{str(Path(__file__).parent.parent)}" + "/" + fileDir + "/" + fileName
    with open(writework, encoding="utf-8", mode="a")as f:
        value = yaml.dump(data, stream=f, allow_unicode=True)
    return value


# 重写post 和get请求，方便自动去请求
def sendRequest(method, url, headers, data):
    # 把请求方法改成小写
    method = str(method).lower()
    rep = None
    # get请求以params接参数
    if method == "get":
        rep = request(method=method, url=url, params=data, headers=headers)
    # post请求以data接参数,原因：data只能传输简单的只有键值对的dict或者str格式的数据，json一般只能传输dict格式，简单复杂的都可以
    # data可以满足多种格式，那我们只需把都转成str类型
    elif method == "post":
        # 把键值对转换成str类型
        rep = request(method=method, url=url, data=json.dumps(data), headers=headers)
        print(rep.request.url)
        print(rep.request.method)
        print(rep.request.body)
    return rep.json()


# 自动分配yaml参数
def assignment_yamlparams(kwargs):
    for key, value in kwargs.items():
        if type(value) is dict:
            assignment_yamlparams(value)
        else:
            if value:
                pass
            else:
                kwargs[key] = getattr(key)
    return kwargs


if __name__ == '__main__':
    work = yaml_read("data", "login.yaml")
    # work =f"{str(Path(__file__).parent.parent)}/data/login.yaml"
    print(work)
