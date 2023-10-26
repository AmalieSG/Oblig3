import pytest
from src/isLeapYear import isLeapYear

def test_years_divisible_by_four_but_not_onehundred_are_leap_years():
    assert isLeapYear(2032)

def test_years_divisible_by_fourhundred_are_leap_years():
    assert isLeapYear(2400)

def test_years_not_divisible_by_four_are_not_leap_years():
    assert not isLeapYear(2001)

def test_years_divisible_by_onehundred_but_not_fourhundred_are_not_leap_years():
    assert not isLeapYear(2100)

# Test med fixture
@pytest.fixture
def years():
    return [1884, 2004, 2012, 2016, 2028, 2036]

def test_years_are_leap_years(years):
    for year in years:
        assert isLeapYear(year)
