"""
==================
Author:Chloeee
Time:2021/4/10 21:56
Contact:403505960@qq.com
==================
"""

import pytest

# 加法参数及用例名称
data_add = [
    [0,0,0],[0.01,0,0.01],[1,0.01,1.01],[1.5,1.5,3],[10000,10000,20000]
]
ids_add = ["测试0加0","测试0加0.01","测试1加0.01","测试小数相加形成整数","测试5位数相加"]


def func_divide(a, b):
    return a / b


def func_multiply(a, b):
    return a*b


def func_minus(a, b):
    return a-b


def func_add(a, b):
    return a+b


class TestCalculator:
    def setup(self):
        print("-------------")
        print("开始计算")

    def teardown(self):
        print("\n 结束计算 \n")
        print("------------")

    @pytest.mark.parametrize("a,b,expect", data_add, ids=ids_add)
    def test_answer_add(self,a,b,expect):
        assert expect == func_add(a,b)

    def test_answer_minus(self):
        assert 4 == func_minus(10,6)

    def test_answer_multiply(self):
        assert 9 == func_multiply(3,3)

    def test_answer_divide(self):
        assert 10 == func_divide(100,10)



