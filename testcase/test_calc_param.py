import json
# from unittest import TestCase
from ddt import ddt, data, file_data, unpack
from src.calc import Calc
import yaml
import pytest



class TestCalc:
    def setup_method(self) -> None:
        self.calc = Calc()



    @pytest.mark.parametrize("a,b,c",[
        (1, 1, 2),
        (1, 2, 3),
        (2, 2, 4)
    ])
    def test_add(self,a,b,c):
        result = self.calc.add(a,b)
        assert c == result

    # @file_data('calc.yaml')
    # @pytest.mark.parametrize("a,b,c",json.load(open('calc.json')))
    @pytest.mark.parametrize("a,b,c", yaml.load(open('/Users/apple/Desktop/AutomatorProject/PyTest/testcase/calc.yaml')))
    def test_div(self,a,b,c):
        # calc = Calc()
        assert self.calc.div(a, b) == c


    def test_above(self):
        # calc = Calc()

        result = self.calc.above(1, 2)
        assert False == result

        result = self.calc.above(2, 2)
        assert False == result
