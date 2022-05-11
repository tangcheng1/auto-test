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
from tools.logger import logger
from pathlib import Path

def init_report():

    # subprocess.call(cmd, shell=True)
    logger.info("""
                     _    _         _      _____         _
      __ _ _ __ (_)  / \\  _   _| |_ __|_   _|__  ___| |_
     / _` | '_ \\| | / _ \\| | | | __/ _ \\| |/ _ \\/ __| __|
    | (_| | |_) | |/ ___ \\ |_| | || (_) | |  __/\\__ \\ |_
     \\__,_| .__/|_/_/   \\_\\__,_|\\__\\___/|_|\\___||___/\\__|
          |_|
          Starting      ...     ...     ...
        """)
    pytest.main(["-s", "test_case/test_admin", "--alluredir=report/data"])
    cmd="allure generate /Users/xu/PycharmProjects/auto_test/report/data -o  /Users/xu/PycharmProjects/auto_test/report/html --clean"
    cmdlog=os.popen(cmd)
    cmdlogs=cmdlog.read()
    print(cmdlogs)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/report/" + "index.html"
    # logger.info("报告地址:{}".format(report_path))



if __name__ == '__main__':
    init_report()