
import unittest
from calc import Calc


class TestCalc(unittest.TestCase):
    def testAdd(self):
        # 1.准备数据
        a = 0
        b = 9
        c = 9
        # 2.调用被测程序
        calc = Calc()
        sum = calc.add(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testsubs(self):
        # 1.准备数据
        a = 9
        b = 9
        c = 0
        # 2.调用被测程序
        calc = Calc()
        sum = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testmulti(self):
        # 1.准备数据
        a = 0
        b = 9
        c = 0
        # 2.调用被测程序
        calc = Calc()
        sum = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testdevision(self):
        # 1.准备数据
        a = 9
        b = 1
        c = 9
        # 2.调用被测程序
        calc = Calc()
        sum = calc.devision(a, b)

        # 3.断言
        self.assertEqual(c, sum)
