from calculator.calculate_rent import RentCalculator
from constants.constants import constant_data_path_env, sample_data_file
import os
import json

if __name__ == "__main__":
    with open(os.path.join(os.environ.get(constant_data_path_env), sample_data_file), 'rb') as f:
        book_data = json.load(f)
        rent_calc = RentCalculator(book_data)
        rent_calc.calculate_rent()
