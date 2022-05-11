import logging
import time
import os
from string import Template

import colorlog
import datetime

import yaml

from tools.yaml_util import YamlUtil
#
# data = YamlUtil().yaml_read("data_yaml", "admin_wallet_add.yaml")
# print(data[0])


import random


def create_phone():
    # 第二位数
    second = [3, 4, 5, 7, 8, 9][random.randint(0, 5)]
    # 第三位数
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
        9: random.randint(0, 9)
    }[second]
    # 最后8位数
    suffix = random.randint(9999999, 100000000)
    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


if __name__ == '__main__':
    print(create_phone())
