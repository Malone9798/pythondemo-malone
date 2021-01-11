import pytest
import yaml
from cal_code import Calculator


def get_datas():
    with open("data.yml") as f:
        datas = yaml.safe_load(f)
        add_datas = datas["add"]
        sub_datas = datas["sub"]
        mul_datas = datas["mul"]
        div_datas = datas["div"]
        return [add_datas, sub_datas, mul_datas, div_datas]

class Testing():

    def setup_class(self):
        self.cal = Calculator()

    def teardown_class(self):
        self.cal = Calculator()

    def setup_testing(self):
        print("开始计算")

    def teardown_testing(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expect", get_datas()[0])
    def test_add(self,a,b,expect):
        result = self.cal.add(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[1])
    def test_sub(self,a,b,expect):
        result = self.cal.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[2])
    def test_mul(self,a,b,expect):
        result = self.cal.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[3])
    def test_div(self,a,b,expect):
        result = self.cal.div(a, b)
        assert result == expect
