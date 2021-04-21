"""
==================
Author:Chloeee
Time:2021/4/17 11:36
Contact:403505960@qq.com
==================
"""

class Calculator:
    @staticmethod
    def func_divide(a, b):
        try:
            result = round(a / b, 2)
        except ZeroDivisionError as e:
            return 'error'
        except TypeError as e:
            return 'error'
        else:
            return result

    @staticmethod
    def func_multiply(a, b):
        return a * b

    @staticmethod
    def func_minus(a, b):
        return a - b

    @staticmethod
    def func_add(a, b):
        return round(a + b, 2)

