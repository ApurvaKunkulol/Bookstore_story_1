__author__ = 'Apurva A Kunkulol'

from constants.constants import rent_per_day


class RentCalculator(object):
    """
    Description: Class for including the functionality to calculate rent based on the books and duration provided.
    """
    def __init__(self, book_duration_data=None):
        if book_duration_data:
            self.book_data = book_duration_data
        else:
            self.book_data = dict()

    def calculate_rent(self):
        """
        Description: Calculate the rent for the books for the given duration.
        """
        total = 0
        if self.book_data:
            for book, duration in self.book_data.items():
                total += (duration * rent_per_day)
            return total
        else:
            raise ValueError("No booknames and durations supplied to calculate rent.")
