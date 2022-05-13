import jsonpath
import pytest
from tools.logger import logger
from tools.yaml_util import YamlUtil
import pytest_check as check
WalletUserName = YamlUtil().yaml_read("config", "config.yaml")['WalletUserName']
res = {'code': '1', 'message': '接口返回成功', 'errMsgParamList': None, 'list': [
    {'id': 63, 'userName': '13315007082', 'nickName': '杜仁艺', 'actualAmt': 85.29, 'couponAmt': 81.03, 'commonAddr': None,
     'couponConfig': None, 'remark': 'fffffffffff', 'createTime': '2022-05-13T03:02:14.000+00:00',
     'updateTime': '2022-05-13T03:02:13.000+00:00', 'businessTel': None, 'businessUid': None},
    {'id': 62, 'userName': '17895069611', 'nickName': '武婷', 'actualAmt': 51.31, 'couponAmt': 45.01, 'commonAddr': None,
     'couponConfig': None, 'remark': 'fffffffffff', 'createTime': '2022-05-13T02:58:59.000+00:00',
     'updateTime': '2022-05-13T02:58:59.000+00:00', 'businessTel': None, 'businessUid': None},
    {'id': 61, 'userName': '14961766515', 'nickName': '符器芝', 'actualAmt': 37.4, 'couponAmt': 31.52, 'commonAddr': None,
     'couponConfig': None, 'remark': 'fffffffffff', 'createTime': '2022-05-12T09:10:38.000+00:00',
     'updateTime': '2022-05-12T09:10:37.000+00:00', 'businessTel': None, 'businessUid': None},
    {'id': 60, 'userName': '17571449978', 'nickName': '郝馥', 'actualAmt': 19.55, 'couponAmt': 14.88, 'commonAddr': None,
     'couponConfig': None, 'remark': 'fffffffffff', 'createTime': '2022-05-12T09:08:25.000+00:00',
     'updateTime': '2022-05-12T09:08:24.000+00:00', 'businessTel': None, 'businessUid': None},
    {'id': 59, 'userName': '18696113766', 'nickName': '桂琼', 'actualAmt': 21.97, 'couponAmt': 11.16, 'commonAddr': None,
     'couponConfig': None, 'remark': 'fffffffffff', 'createTime': '2022-05-12T09:04:35.000+00:00',
     'updateTime': '2022-05-12T09:04:34.000+00:00', 'businessTel': None, 'businessUid': None},
    {'id': 57, 'userName': '18445439289', 'nickName': '范仁月', 'actualAmt': 44.54, 'couponAmt': 34.34, 'commonAddr': None,
     'couponConfig': None, 'remark': 'fffffffffff', 'createTime': '2022-05-12T09:02:38.000+00:00',
     'updateTime': '2022-05-12T09:02:38.000+00:00', 'businessTel': None, 'businessUid': None},
    {'id': 56, 'userName': '15916360928', 'nickName': '郎娜', 'actualAmt': 44.8, 'couponAmt': 42.44, 'commonAddr': None,
     'couponConfig': None, 'remark': 'fffffffffff', 'createTime': '2022-05-12T08:59:14.000+00:00',
     'updateTime': '2022-05-12T08:59:14.000+00:00', 'businessTel': None, 'businessUid': None},
    {'id': 55, 'userName': '13324741132', 'nickName': '何无竹', 'actualAmt': 92.51, 'couponAmt': 86.54, 'commonAddr': None,
     'couponConfig': None, 'remark': 'fffffffffff', 'createTime': '2022-05-12T08:56:41.000+00:00',
     'updateTime': '2022-05-12T08:56:40.000+00:00', 'businessTel': None, 'businessUid': None},
    {'id': 54, 'userName': '15554560309', 'nickName': '沃礼华', 'actualAmt': 16.24, 'couponAmt': 12.62, 'commonAddr': None,
     'couponConfig': None, 'remark': 'fffffffffff', 'createTime': '2022-05-12T08:48:51.000+00:00',
     'updateTime': '2022-05-12T08:48:51.000+00:00', 'businessTel': None, 'businessUid': None},
    {'id': 53, 'userName': '13929692104', 'nickName': '姜瑗', 'actualAmt': 53.41, 'couponAmt': 49.12, 'commonAddr': None,
     'couponConfig': None, 'remark': 'fffffffffff', 'createTime': '2022-05-12T08:39:30.000+00:00',
     'updateTime': '2022-05-12T08:39:29.000+00:00', 'businessTel': None, 'businessUid': None}], 'success': True}
reslist = res['list']

# print(jsonpath.jsonpath(res,'$.list[?(@.id==54).userName]'))
#
# if "139" in str(reslist):
#     print("qqqqqqq")
list=[]
for i in reslist:
    # print("333")
    list.append(i.values())
print(list)
# print(i.values())
print("13315007082" in list)

#     print("11111")
# else:
#     print("2222")
    # if "1392969210" in i.values():
    #     # list(i.keys())[list(i.values()).index('13929692104')]
    #     if str(13929692104) == i['userName']:
    #         check.equal(i['actualAmt'], float(53.41))
    #         check.equal(i['couponAmt'], float(49.12))
    #         logger.info("ddd{}".format(i['userName']))
    #     else:
    #         logger.info("充值金额{}".format(i['userName']))



