import decimal
import random
from decimal import Decimal
import jsonpath
import pytest

from tools.base_requests import Utils
from tools.logger import logger
from tools.yaml_util import YamlUtil
import pytest_check as check
#
# response={'code': '1', 'message': '接口返回成功', 'errMsgParamList': None, 'list': [{'id': 113, 'bizType': 1, 'userId': 76, 'userName': '17530285529', 'totalChangeAmt': 10.0, 'actualAmt': 10.0, 'couponAmt': 0.0, 'remainActualAmt': 86.64, 'remainCouponAmt': 75.38, 'remark': None, 'businessUid': None, 'tagId': None, 'createTime': '2022-05-16T03:49:06.000+00:00', 'updateTime': '2022-05-16T03:49:05.000+00:00', 'businessTel': None, 'businessName': None}, {'id': 112, 'bizType': 1, 'userId': 76, 'userName': '17530285529', 'totalChangeAmt': 152.02, 'actualAmt': 76.64, 'couponAmt': 75.38, 'remainActualAmt': 76.64, 'remainCouponAmt': 75.38, 'remark': None, 'businessUid': None, 'tagId': None, 'createTime': '2022-05-16T03:49:01.000+00:00', 'updateTime': '2022-05-16T03:49:01.000+00:00', 'businessTel': None, 'businessName': None}], 'success': True}
# reslist = response['list']
# i = reslist[0]
# print(i['userName'])
#
# actualamt = decimal.Decimal(str(random.randint(10, 100)) + '.' + str(random.randint(0, 99)))
# print("随机获取充值金额{}".format(actualamt))
# print(type(actualamt))
#
#
# a=74.49
# b=decimal.Decimal(a)+10
# print(type(b))


#
# a=Decimal(str(15.1))
# print(a)

check.aequal("12.12", "12.11" ,"充值金额断言")
check.aequaal("12.12", "12.11" ,"充值金额断言")