# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : conftest.py.py
# @Author   : Pluto.
# @Time     : 2020/9/18 15:55
#pytest用例ids显示中文
from typing import List
def pytest_collection_modifyitems(items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
