from main import is_leap_year

def test_pytest():
    assert 3+3 ==6

def test_divisible_by_400():
    assert is_leap_year(2000) == True

def test_not_divisible_by_4():
    assert is_leap_year(2023) == False
    assert is_leap_year(2019) == False

def test_divisible_by_100_not_400():
    assert is_leap_year(1900) == False
    assert is_leap_year(2300) == False

def test_divisible_by_4_not_100():
    assert is_leap_year(2024) == True
    assert is_leap_year(2028) == True