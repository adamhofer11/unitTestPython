import unittest
import re
from datetime import datetime


def validate_symbol(symbol):
    return bool(re.fullmatch(r'[A-Z]{1,7}', symbol))

def validate_chart_type(chart_type):
    return chart_type in {'1', '2'}

def validate_time_series(time_series):
    return time_series in {'1', '2', '3', '4'}

def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

#unit test
class TestProject3Inputs(unittest.TestCase):

    # Symbol Tests
    def test_valid_symbol(self):
        self.assertTrue(validate_symbol('AAPL'))
        self.assertTrue(validate_symbol('GOOGL'))
        self.assertTrue(validate_symbol('TSLA'))

    def test_invalid_symbol(self):
        self.assertFalse(validate_symbol('appl'))  # lowercase
        self.assertFalse(validate_symbol('AAPL1'))  # contains number
        self.assertFalse(validate_symbol('LONGSYMBOL'))  # too long

    # Chart Type Tests
    def test_valid_chart_type(self):
        self.assertTrue(validate_chart_type('1'))
        self.assertTrue(validate_chart_type('2'))

    def test_invalid_chart_type(self):
        self.assertFalse(validate_chart_type('3'))
        self.assertFalse(validate_chart_type('a'))
        self.assertFalse(validate_chart_type(''))

    # Time Series Tests
    def test_valid_time_series(self):
        self.assertTrue(validate_time_series('1'))
        self.assertTrue(validate_time_series('2'))
        self.assertTrue(validate_time_series('3'))
        self.assertTrue(validate_time_series('4'))

    def test_invalid_time_series(self):
        self.assertFalse(validate_time_series('5'))
        self.assertFalse(validate_time_series('0'))
        self.assertFalse(validate_time_series('a'))

    # Start Date Tests
    def test_valid_start_date(self):
        self.assertTrue(validate_date('2024-01-01'))
        self.assertTrue(validate_date('2023-12-31'))

    def test_invalid_start_date(self):
        self.assertFalse(validate_date('01-01-2024'))  
        self.assertFalse(validate_date('2024/01/01'))  
        self.assertFalse(validate_date('2024-13-01'))  

    # End Date Tests
    def test_valid_end_date(self):
        self.assertTrue(validate_date('2025-04-25'))
        self.assertTrue(validate_date('2024-06-30'))

    def test_invalid_end_date(self):
        self.assertFalse(validate_date('25-04-2025'))
        self.assertFalse(validate_date('2025/04/25'))
        self.assertFalse(validate_date('2025-02-30'))  

if __name__ == '__main__':
    unittest.main()
