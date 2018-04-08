__author__ = 'Apurva A Kunkulol'

import unittest
from unittest.mock import patch
from calculator.calculate_rent import RentCalculator
from constants.constants import sample_data_file, constant_data_path_env
import json
import os


class TestRentCalculator(unittest.TestCase):
    def setUp(self):
        file_path = os.path.join(os.environ.get(constant_data_path_env), sample_data_file)
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
        self.assertEqual(self.calculator.calculate_rent(), 10.5)


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
        self.assertEqual(self.calculator.calculate_rent(), 11.25)

    def test_misformed_data(self):
        test_book_data = {
            "sample_book_title": 1,
            "sample_book_title_1": None,
            "sample_book_title_2": 3.5
        }
        self.calculator = RentCalculator(test_book_data)
        self.assertRaises(TypeError, self.calculator.calculate_rent)

    def test_modified_rent_info(self):
        test_book_data = {
            "sample_book_title": 5,
            "sample_book_title_1": 2.5,
            "sample_book_title_2": 3.5
        }
        test_rent_data = {
            "sample_book_title": {"book_type": "fiction", "rent": 3},
            "sample_book_title_1": {"book_type": "regular", "rent": 1.5},
            "sample_book_title_2": {"book_type": "novel", "rent": 1.5}
        }
        self.calculator = RentCalculator(test_book_data)
        self.calculator.rent_data = test_rent_data
        self.assertEqual(self.calculator.calculate_rent(), 24)

    def test_missing_charges(self):
        test_book_data = {
            "sample_book_title": 5,
            "sample_book_title_1": 2.5,
            "sample_book_title_2": 3.5
        }
        test_rent_data = {
            "sample_book_title": {"book_type": "fiction", "rent": 3},
            "sample_book_title_1": {"book_type": "regular", "rent": None},
            "sample_book_title_2": {"book_type": "novel", "rent": 1.5}
        }
        self.calculator = RentCalculator(test_book_data)
        self.calculator.rent_data = test_rent_data
        self.assertRaises(ValueError, self.calculator.calculate_rent)

    def test_missing_type_rent_info(self):
        test_book_data = {
            "sample_book_title": 5,
            "sample_book_title_1": 2.5,
            "sample_book_title_2": 3.5
        }
        test_rent_data = {
            "sample_book_title": {"book_type": "fiction", "rent": 3},
            "sample_book_title_1": None,
            "sample_book_title_2": {"book_type": "novel", "rent": 1.5}
        }
        self.calculator = RentCalculator(test_book_data)
        self.calculator.rent_data = test_rent_data
        self.assertRaises(ValueError, self.calculator.calculate_rent)


if __name__ == "__main__":
    unittest.main()
