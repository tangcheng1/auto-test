#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 09:48
# @Author  : tc
# @File    : run.py
# @Description :
import os
import time

import pytest,os,subprocess
import  allure

from pathlib import Path

def init_report():

    # subprocess.call(cmd, shell=True)
    cmd="allure generate /Users/xu/PycharmProjects/auto_test/result -o  /Users/xu/PycharmProjects/auto_test/report --clean"
    cmdlog=os.popen(cmd)
    cmdlogs=cmdlog.read()
    print(cmdlogs)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/report/" + "index.html"
    # logger.info("报告地址:{}".format(report_path))



# pytest.main(["-s","--reruns=2", "android/testcase","--alluredir=data_yaml"])
pytest.main(["-s", "test_case","--alluredir=result"])
init_report()
