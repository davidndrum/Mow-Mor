"""
Program: mowingCustomer.py
Author: David Drummond

This module declares a class to define a customer's data.

"""

class Customer:
    """Class that sets the expected values for a customer record."""

    def __init__(self, first, last, streetNumber, streetName, city, stateID, zipCode, timePreference, weekdayPreference):
        self.first = first
        self.last = last
        self.streetNumber = streetNumber
        self.streetName = "  " + streetName
        self.city = city
        self.stateID = stateID
        self.zipCode = zipCode
        self.timePreference = int(timePreference)
        self.weekdayPreference = weekdayPreference

    def __str__(self):
        """This creates a function that puts the entire record in a string."""

        return("%-10s%-20s%6s%20s%20s%3s%9d%5d%5s" % (self.first, self.last, self.streetNumber, self.streetName, self.city, self.stateID, int(self.zipCode), int(self.timePreference), self.weekdayPreference))


