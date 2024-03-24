from rapidgbm.utility.validatormixin import ArgValidationMixin

def test_is_bool():
    assert ArgValidationMixin._is_bool(True) == True
    assert ArgValidationMixin._is_bool(False) == True
    assert ArgValidationMixin._is_bool(1) == False
    assert ArgValidationMixin._is_bool('hello world') == False

def test_is_int():
    assert ArgValidationMixin._is_int(1) == True
    assert ArgValidationMixin._is_int(-1) == True
    assert ArgValidationMixin._is_int(1.0) == False
    assert ArgValidationMixin._is_int('hello world') == False



