"""
==================
Author:Chloeee
Time:2021/4/10 21:56
Contact:403505960@qq.com
==================
"""

import pytest

# 加法数据及用例名称
data_add = [
    [0,0,0],[0.01,0,0.01],[1,0.01,1.01],[1.5,1.5,3],[10000,10000,20000]
]
ids_add = ["测试0加0","测试0加0.01","测试1加0.01","测试小数相加形成整数","测试5位数相加"]

# 除法数据及用例名称
data_divide = [
    [300,3,100], [100,3,33.33], [100,6,16.67], [3,2,1.5], [5,4,1.25],[0.2,0.02,10],
    [3,0,'error'],[0,3,0],['abc',0,'error']
]
ids_divide = ["测试整除", "测试无限小数-不四舍五入", "测试无效小数-四舍五入",
              "测试结果一位小数", "测试结果两位小数","测试小数相除","除以0","0除以整数","除数有字符串"]



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
    return a + b


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

    @pytest.mark.parametrize("a,b,expect", data_divide, ids=ids_divide)
    def test_answer_divide(self,a,b,expect):
        assert expect == func_divide(a,b)



