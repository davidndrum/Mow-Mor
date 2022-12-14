"""
mowingCustomer.py

This module declares a class to define a customer's data.

"""

class Customer:
    """Class that sets the expected values for a customer record."""

    def __init__(self, first, last, streetNumber, streetName, city, stateID, zipCode, timePreference, weekdayPreference):
        self.first = first
        self.last = last
        self.streetNumber = streetNumber
        self.streetName = streetName
        self.city = city
        self.stateID = stateID
        self.zipCode = zipCode
        self.timePreference = timePreference
        self.weekdayPreference = weekdayPreference

    def createdRecord(self):

        return (str('{} {} {} {} {} {} {} {} {}'.format(self.first, self.last, self.streetNumber, self.streetName, self.city, self.stateID, self.zipCode, self.timePreference, self.weekdayPreference)))

#    def printRecord(self):
#        print(self.createdRecord())

cust_1 = Customer('David', 'Drummond', '485', 'W. Mechanic St', 'Shelbyville', 'IN', '46176', 'Morning', 'TH')

print(cust_1.createdRecord())
