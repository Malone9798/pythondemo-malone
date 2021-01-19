import pytest
import yaml
class Testing:
    @pytest.mark.first
    def test_add(self,get_calc,get_data):
        try:
            result = get_calc.add(get_data["add"][0],get_data["add"][1])
            if isinstance(result,float):
                result = round(result,9)
        except Exception as e:
            result = "请输入数字"
        assert result == get_data["add"][2]


    @pytest.mark.run(order=3)
    def test_sub(self,get_calc,get_data):
        try:
            result = get_calc.add(get_data["sub"][0],get_data["sub"][1])
            if isinstance(result,float):
                result = round(result,9)
        except Exception as e:
            result = "请输入数字"
        assert result == get_data["sub"][2]

    @pytest.mark.run(order=4)
    def test_mul(self,get_calc,get_data):
        try:
            result = get_calc.add(get_data["mul"][0],get_data["mul"][1])
            if isinstance(result,float):
                result = round(result,9)
        except Exception as e:
            result = "请输入数字"
        assert result == get_data["mul"][2]

    @pytest.mark.second
    def test_div(self,get_calc,get_data):
        try:
            result = get_calc.add(get_data["div"][0],get_data["div"][1])
            if isinstance(result,float):
                result = round(result,9)
        except Exception as e:
            result = "请输入数字"
        except ZeroDivisionError:
            result = "除数不能为0"
        assert result == get_data["div"][2]