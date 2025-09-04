import unittest

def convert_date_format(date_str):
    # Assumes input is in "YYYY-MM-DD"
    try:
        parts = date_str.split('-')
        if len(parts) != 3:
            raise ValueError
        yyyy, mm, dd = parts
        if len(yyyy) != 4 or len(mm) != 2 or len(dd) != 2:
            raise ValueError
        return f"{dd}-{mm}-{yyyy}"
    except Exception:
        return "Invalid input"

class TestConvertDateFormat(unittest.TestCase):
    def test_standard_dates(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")
        self.assertEqual(convert_date_format("1999-01-01"), "01-01-1999")
        self.assertEqual(convert_date_format("2000-12-31"), "31-12-2000")
        self.assertEqual(convert_date_format("2020-02-29"), "29-02-2020")  # Leap year

    def test_invalid_format(self):
        self.assertEqual(convert_date_format("2023/10/15"), "Invalid input")
        self.assertEqual(convert_date_format("15-10-2023"), "Invalid input")
        self.assertEqual(convert_date_format("2023-1-5"), "Invalid input")
        self.assertEqual(convert_date_format("20231015"), "Invalid input")
        self.assertEqual(convert_date_format(""), "Invalid input")
        self.assertEqual(convert_date_format("2023-10"), "Invalid input")
        self.assertEqual(convert_date_format("2023-10-15-01"), "Invalid input")

    def test_non_string_input(self):
        self.assertEqual(convert_date_format(None), "Invalid input")
        self.assertEqual(convert_date_format(20231015), "Invalid input")
        self.assertEqual(convert_date_format(["2023-10-15"]), "Invalid input")

if __name__ == "__main__":
    unittest.main()

