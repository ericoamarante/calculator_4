from .calculator_4 import Calculator4
from pytest import raises
from typing import Dict, List

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate_with_body_error():
    mock_request = MockRequest({"numbersss" : [1, 2, 3]})
    calculator_4 =Calculator4()

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == "Body mal formatado!"

def test_calculate():
    mock_request = MockRequest({"numbers" : [1, 2, 3, 4, 5]})
    calculator_4 = Calculator4()

    response = calculator_4.calculate(mock_request)

    assert response['data']['Calculator'] == 4
    assert response['data']['result'] == 3
    assert response['data']['Success'] == True