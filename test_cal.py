"""
==================
Author:Chloeee
Time:2021/4/10 21:56
Contact:403505960@qq.com
==================
"""

from data.calculator import data_add_int,data_divide,data_add_float,ids_add_int,ids_divide,ids_add_float
from pages.calculator import Calculator
import pytest
import allure





@allure.feature("测试计算器")
@pytest.mark.usefixtures("calculate_func")
class TestCalculator:
    # def setup(self):
    #     print("-------------")
    #     print("开始计算")

    # def teardown(self):
    #     print("\n 结束计算 \n")
    #     print("------------")


    # @pytest.mark.parametrize("a,b,expect", data_add_int, ids=ids_add_int)
    # 使用fixture参数
    @allure.story("测试int情况")
    @pytest.mark.run(order=2)
    def test_answer_add_int(self,prepare_add_int):
        """测试int的情况"""
        a, b, expect = prepare_add_int
        assert expect == Calculator.func_add(a,b)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect", data_add_float, ids=ids_add_float)
    def test_answer_add_float(self,a,b,expect):
        """测试float的情况"""
        assert expect == Calculator.func_add(a, b)

    @pytest.mark.parametrize("a,b,expect", data_divide, ids=ids_divide)
    def test_answer_divide(self,a,b,expect):
        assert expect == Calculator.func_divide(a,b)

    def test_answer_minus(self):
        assert 4 == Calculator.func_minus(10,6)

    def test_answer_multiply(self):
        assert 9 == Calculator.func_multiply(3,3)


