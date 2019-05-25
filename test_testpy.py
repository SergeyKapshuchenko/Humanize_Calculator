import pytest
from HumanizeCalculator import hum_calc as HC

def test_case_1():
    assert HC("100 + 222 = 3") == "one hundred plus two hundred twenty two equals three"

def test_case_2():
    assert HC("1 * 125 = 125") == "one multiply one hundred twenty five equals one hundred twenty five"

def test_case_3():
    assert HC("1000325 / 125342 = 15") == "one million, three hundred twenty five divide by one hundred twenty five thousand, three hundred forty two equals fifteen"

def test_case_4():
    assert HC("123456 * 999 = 1546") == "one hundred twenty three thousand, four hundred fifty six multiply nine hundred ninety nine equals one thousand, five hundred forty six"

def test_case_5():
    assert HC("15 * 4 = 60") == "fifteen multiply four equals sixty"

def test_case_6():
    assert HC("5 - 0 = 5") == "five minus zero equals five"

def test_case_7():
    assert HC("115 + 162 = 277") == "one hundred fifteen plus one hundred sixty two equals two hundred seventy seven"

def test_case_8():
    assert HC("1000001 * 1001 = 15") == "one million, one multiply one thousand, one equals fifteen"

def test_case_9():
    assert HC("1025 / 25 = 41") == "one thousand, twenty five divide by twenty five equals forty one"

def test_case_10():
    assert HC("11 *100=1100") == "eleven multiply one hundred equals one thousand, one hundred"

def test_exception_1():
    with pytest.raises(ValueError):
        HC("1s + 2 = b)")

def test_exception_2():
    with pytest.raises(ValueError):
        HC("1000000000000 + 125 = 1000000000125")
