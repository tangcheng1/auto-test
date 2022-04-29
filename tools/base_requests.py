import json

import xlrd
import yaml
from requests import request

#读取excel
def excel_read():
    book = xlrd.open_workbook("../data/case_data1.xls")
                    # 读取第一个sheet页
    sheet = book.sheet_by_index(0)
    list =[]
    for norw in range(1, sheet.nrows):
            # if sheet.cell_value(norw, 4) != "否":  # 每行第4列等于否将不读取内容

            dict_case = dict (
            url = sheet.cell_value(norw,3),
            headers=sheet.cell_value(norw,2),
            method = sheet.cell_value(norw,5),
            data  = sheet.cell_value(norw,8))
            list.append(dict_case)
            # value = table.row_values(norw)
            # value = table.col_values(norw)
            # value.pop(4)   #删除是否的那一列
    # print(list)
    return list


# 读取yaml
def yaml_read():
    with open('../data/login.yaml',encoding='utf-8',) as f:
          value = yaml.load(f,Loader=yaml.FullLoader)
          # print(value["request"])
    return value


 # 重写post 和get请求，方便自动去请求
def sendRequest(method,url,headers,data):
        #把请求方法改成小写
        method = str(method).lower()
        rep = None
        #get请求以params接参数
        if method == "get":
            rep = request(method=method, url=url, params=data,headers=headers)
        # post请求以data接参数,原因：data只能传输简单的只有键值对的dict或者str格式的数据，json一般只能传输dict格式，简单复杂的都可以
        #data可以满足多种格式，那我们只需把都转成str类型
        elif method=="post":
            # 把键值对转换成str类型
            rep = request(method=method, url=url, data=json.dumps(data),headers=headers)
        return rep.json()