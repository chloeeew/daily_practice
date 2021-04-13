"""
==================
Author:Chloeee
Time:2021/4/11 11:46
Contact:403505960@qq.com
==================
"""

import pytest
from typing import List

def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

