"""
==================
Author:Chloeee
Time:2021/4/10 21:56
Contact:403505960@qq.com
==================
"""

from data.calculator import data_add_int,data_divide,data_add_float,ids_add_int,ids_divide,ids_add_float
import pytest





def func_divide(a, b):
    try:
        result = round(a / b, 2)
    except ZeroDivisionError as e:
        return 'error'
    except TypeError as e:
        return 'error'
    else:
        return result


def func_multiply(a, b):
    return a * b


def func_minus(a, b):
    return a - b


def func_add(a, b):
    return round(a + b, 2)


class TestCalculator:
    def setup(self):
        print("-------------")
        print("开始计算")

    def teardown(self):
        print("\n 结束计算 \n")
        print("------------")

    @pytest.mark.parametrize("a,b,expect", data_add_int, ids=ids_add_int)
    def test_answer_add_int(self,a,b,expect):
        """测试int的情况"""
        assert expect == func_add(a,b)

    @pytest.mark.parametrize("a,b,expect", data_add_float, ids=ids_add_float)
    def test_answer_add_float(self,a,b,expect):
        """测试float的情况"""
        assert expect == func_add(a, b)

    def test_answer_minus(self):
        assert 4 == func_minus(10,6)

    def test_answer_multiply(self):
        assert 9 == func_multiply(3,3)

    @pytest.mark.parametrize("a,b,expect", data_divide, ids=ids_divide)
    def test_answer_divide(self,a,b,expect):
        assert expect == func_divide(a,b)



