import json
from tools.logger import logger
import xlrd
from requests import request
from tools.yaml_util import YamlUtil


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

# 重写post 和get请求，方便自动去请求
def sendRequest(method, url, data,headers,**kwargs):

    # 把请求方法改成小写
    method = str(method).lower()
    rep = None
    # get请求以params接参数
    request_log(method,url,data,headers)
    if method == "get":
        rep = request(method=method, url=url, params=data, headers=headers,**kwargs)
    # post请求以data接参数,原因：data只能传输简单的只有键值对的dict或者str格式的数据，json一般只能传输dict格式，简单复杂的都可以
    # data可以满足多种格式，那我们只需把都转成str类型
    elif method == "post":
        # 把键值对转换成str类型
        data = json.dumps(data)
        rep = request(method=method, url=url, data=data, headers=headers,**kwargs)
    logger.info("返回的body ==>> {}".format(rep.json()))
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

def request_log( method, url, data=None,  headers=None, files=None, cookies=None,**kwargs):
    logger.info("接口请求地址 ==>> {}".format(url))
    logger.info("接口请求方式 ==>> {}".format(method))
    logger.info("接口请求体body ==>> {}".format(json.dumps(data, indent=4, ensure_ascii=False)))
    # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
    logger.info("接口请求头 ==>> {}".format(headers, indent=4, ensure_ascii=False))
    # logger.info("接口请求 params 参数 ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
    #
    #
    # logger.info("接口上传附件 files 参数 ==>> {}".format(files))
    # logger.info("接口 cookies 参数 ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))

    # (method=method, url=url, data=data, headers=headers, ** kwargs)
if __name__ == '__main__':
    work = YamlUtil().yaml_read("data", "login.yaml")
    # work =f"{str(Path(__file__).parent.parent)}/data/login.yaml"
    print(work)

