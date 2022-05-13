#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 14:27
# @Author  : tc
# @File    : calculation_function.py
# @Description :
import random
import decimal

# #
# a = str(random.randint(0,100))
# #
# b=str(random.randint(0,99))
# c = a+'.'+b
# d = float(c)
#
# # print(random.random())

# 随机获取充值金额
actualamt = decimal.Decimal(str(random.randint(10, 100)) + '.' + str(random.randint(0, 99)))
print("随机获取充值金额{}".format(actualamt))
# 随机获取的数字
randomnum = decimal.Decimal(str(random.randint(1, 10)) + '.' + str(random.randint(0, 99)))
print("随机获取的数字{}".format(randomnum))
# 比充值金额少的值
numamt_smaller = actualamt - randomnum
print("比充值金额少的值{}".format(numamt_smaller))
# 比充值金额大的值
numamt_bigger = actualamt + randomnum
print("比充值金额大的值{}".format(numamt_bigger))


# 随机的优惠金额
couponAmt = numamt_smaller
print("随机的优惠金额{}".format(couponAmt))

# 充值金额+优惠金额
totalChangeAmt = couponAmt + actualamt
print("充值金额+优惠金额{}".format(totalChangeAmt))

