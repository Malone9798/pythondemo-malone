import pytest
import yaml

from calculator import Calculator

with open("data.yml") as f:
    data = yaml.safe_load(f)
    print(data)

@pytest.fixture(scope="moudle")
def get_calc(request):
    print("开始计算")
    cal = Calculator()
    yield
    print("结束计算")

@pytest.fixture(params=data)
def get_data(request):
    data = request.param
    yield data