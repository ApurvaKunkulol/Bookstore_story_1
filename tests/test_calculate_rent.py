__author__ = 'Apurva A Kunkulol'

import unittest
from calculator.calculate_rent import RentCalculator
from constants.constants import sample_data_file
import json
import os


class TestRentCalculator(unittest.TestCase):
    def setUp(self):
        file_path = os.path.join(os.environ.get("bookstore_sample_data"), sample_data_file)
        self.sample_data_file = open(file_path, 'rb')
        self.test_book_data = json.load(self.sample_data_file)
        self.calculator = RentCalculator(self.test_book_data)

    def tearDown(self):
        self.sample_data_file.close()
        del self.calculator

    def test_all_data(self):
        """
            Description: Verify if the value of rent is as expected, when all data is supplied in proper format.
        """
        self.assertEqual(self.calculator.calculate_rent(), 6)


    def test_no_data(self):
        self.calculator = RentCalculator()
        self.assertRaises(ValueError, self.calculator.calculate_rent)

    def test_half_days(self):
        test_book_data = {
            "sample_book_title": 1,
            "sample_book_title_1": 2,
            "sample_book_title_2": 3.5
        }
        self.calculator = RentCalculator(test_book_data)
        self.assertEqual(self.calculator.calculate_rent(), 6.5)

    def test_misformed_data(self):
        test_book_data = {
            "sample_book_title": 1,
            "sample_book_title_1": None,
            "sample_book_title_2": 3.5
        }
        self.calculator = RentCalculator(test_book_data)
        self.assertRaises(TypeError, self.calculator.calculate_rent)


if __name__ == "__main__":
    unittest.main()
