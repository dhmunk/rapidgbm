from rapidgbm.utility.validatormixin import ValidationMixin

def test_is_bool():
    assert ValidationMixin._is_bool(True) == True
    assert ValidationMixin._is_bool(False) == True
    assert ValidationMixin._is_bool(1) == False
    assert ValidationMixin._is_bool('hello world') == False

def test_is_int():
    assert ValidationMixin._is_int(1) == True
    assert ValidationMixin._is_int(-1) == True
    assert ValidationMixin._is_int(1.0) == False
    assert ValidationMixin._is_int('hello world') == False



