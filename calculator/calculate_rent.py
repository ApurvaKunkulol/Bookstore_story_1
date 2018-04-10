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
            #import pdb
            #pdb.set_trace()
            print("\nBook\t\t   Duration    Rent")
            print("--------------------------------------")
            for book, duration in self.book_data.items():
                rent_info = self.rent_data.get(book)
                if rent_info:
                    min_duration, min_charge = rent_info.get("minimum_duration", 0), rent_info.get("minimum_charges", 0)
                    minimum_rent = 0
                    if min_duration and min_charge:
                        minimum_rent = min_duration * min_charge
                    rent = 0
                    if duration is not None and 0 < duration > min_duration:
                        if not rent_info.get("regular_rent"):
                            raise ValueError("Regular rent charges not specified.")
                        rent = rent_info.get("regular_rent") * (duration - min_duration)
                    print("{}\t{}\t{}".format(book, duration, (rent + minimum_rent)))
                    total_rent += (rent + minimum_rent)
                else:
                    raise ValueError("Rent information not available for '{}'.".format(book))
            print("--------------------------------------")
            print("Total Rent:\t\t{}".format(total_rent))
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
