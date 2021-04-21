"""
==================
Author:Chloeee
Time:2021/4/11 11:46
Contact:403505960@qq.com
==================
"""

from pytestdemo.data.calculator import data_add_int,ids_add_int
import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# 添加命令行参数 --env 切换环境测试数据
def pytest_addoption(parser):
    parser.addoption("--env", action="store",
                     default="release",
                     help="根据环境切换测试数据，release==测试环境//master==业务环境")

@pytest.fixture(scope='session',autouse=True)
def envir(request):
    myenv = request.config.getoption("--env")
    if myenv == "release":
        print("测试环境数据")
    elif myenv == 'master':
        print("业务环境测试数据")
    else:
        print('没有测试数据')



@pytest.fixture()
def calculate_func():
    print("-------------")
    print("开始计算")
    yield
    print('计算结束')
    print("-------------")


@pytest.fixture(params=data_add_int,ids=ids_add_int)
def prepare_add_int(request):
    yield request.param



