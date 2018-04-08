from constants.constants import rent_data, constant_data_path_env
import os
import json


class RentCalculator(object):
    """
    Description: Class for including the functionality to calculate rent based on the books and duration provided.
    """
    def __init__(self, book_duration_data=None):
        if book_duration_data:
            self.book_data = book_duration_data
        else:
            self.book_data = dict()
        self.rent_data = self.load_rent_data()

    def calculate_rent(self):
        """
        Description: Calculate the rent for the books for the given duration.
        """
        total_rent = 0
        if self.book_data:
            for book, duration in self.book_data.items():
                rent_info = self.rent_data.get(book)
                if rent_info:
                    charges = rent_info.get("rent")
                    if charges:
                        total_rent += (duration * charges)
                    else:
                        raise ValueError("Charges not specified for book type: {}".format(rent_info.get("book_type")))
                else:
                    raise ValueError("Rent information not available for '{}'.".format(book))
            return total_rent
        else:
            raise ValueError("No book names and durations supplied to calculate rent.")

    def load_rent_data(self):
        """
            Description: Function to load the rent data for calculation.
        """
        rent_data_filepath = os.path.join(os.environ.get(constant_data_path_env), rent_data)
        with open(rent_data_filepath, "rb") as fhandle:
            return json.load(fhandle)
