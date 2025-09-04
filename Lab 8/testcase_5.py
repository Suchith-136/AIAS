from Task_5 import convert_date_format

def test_convert_date_format_basic():
    assert convert_date_format("2023-10-15") == "15-10-2023"

def test_convert_date_format_single_digit_month_day():
    assert convert_date_format("2024-01-05") == "05-01-2024"

def test_convert_date_format_leap_year():
    assert convert_date_format("2020-02-29") == "29-02-2020"

def test_convert_date_format_end_of_year():
    assert convert_date_format("1999-12-31") == "31-12-1999"

def test_convert_date_format_beginning_of_year():
    assert convert_date_format("2000-01-01") == "01-01-2000"